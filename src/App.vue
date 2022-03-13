<script>
import AddonList from "@/components/AddonList.vue";
import AddonDetails from "@/components/AddonDetails.vue";
import HeaderBar from "@/components/HeaderBar.vue";

export default {
  data() {
    return {
      addons: {},
      currentAddon: {},
      sorting: 'total'
    }
  },
  methods: {
    loadAddonData() {
      fetch("/addons.json", {
        method: "get"
      })
          .then(response => {
            this.onDataLoaded(response.json())
          })
          .catch(error => {
            console.error("Error on retrieving data", error)
          })
    },
    onDataLoaded(dataPromise) {
      dataPromise.then(json => {
        for (const addonKey in json) {
          json[addonKey]['name'] = addonKey;
        }
        this.addons = json
        this.addonClicked(Object.keys(this.addons)[0])
      })
    },
    addonClicked(addonKey) {
      this.currentAddon = this.addons[addonKey]
    }
  },
  computed: {
    addonsLoaded() {
      return this.addons !== undefined && Object.keys(this.addons).length > 0;
    },
    reactiveAddons() {
      let compareFunction
      if (this.sorting === 'total') {
        compareFunction = (one, two) => two.total - one.total;
      } else if (this.sorting === 'name') {
        compareFunction = (one, two) => {
          return (one.name < two.name ? -1 : (one.name > two.name ? 1 : 0));
        }
      }
      let sortedAddonsArray = Object.values(this.addons).sort(compareFunction)

      const sortedAddons = {}
      for (const addon of sortedAddonsArray) {
        sortedAddons[addon.name] = addon;
      }
      return sortedAddons;
    }
  },
  components: {
    HeaderBar,
    AddonList,
    AddonDetails,
  },
  beforeMount() {
    this.loadAddonData()
  }
}
</script>

<template>
  <HeaderBar/>
  <div class="container">
    <div class="row" v-if="addonsLoaded">
      <div class="col-4 list">
        <AddonList :addon-data="this.reactiveAddons" :current-addon="this.currentAddon"
                   @addon-clicked="(addon) => addonClicked(addon)" @change-sorting="(newSorting) => this.sorting = newSorting"/>
      </div>
      <div class="col-8">
        <AddonDetails :addon-details="this.currentAddon"/>
      </div>
    </div>
    <div class="text-center" v-if="!addonsLoaded">
      <div class="spinner-border text-primary d-inline-block" role="status">
        <span class="visually-hidden">Loading...</span>
      </div>
    </div>
  </div>
</template>
