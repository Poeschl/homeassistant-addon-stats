<script>
import AddonList from "@/components/AddonList.vue";
import AddonDetails from "@/components/AddonDetails.vue";
import HeaderBar from "@/components/HeaderBar.vue";

export default {
  data() {
    return {
      addons: {},
      currentAddon: {},
      sorting: 'total',
      filter: ''
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
        this.checkForFilterParam()
        this.addonClicked(Object.keys(this.reactiveAddons)[0])
      })
    },
    addonClicked(addonKey) {
      this.currentAddon = this.addons[addonKey]
    },
    checkForFilterParam() {
      let queryString = window.location.search;
      let urlParams = new URLSearchParams(queryString);
      if (urlParams.has("filter")) {
        this.filter = urlParams.get("filter")
      }
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
      let sortedAddonsArray = Object.values(this.addons)
        .filter(addon => addon.name.includes(this.filter))
        .sort(compareFunction)

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
  mounted() {
    this.loadAddonData()
  }
}
</script>

<template>
  <HeaderBar/>
  <div class="container">
    <div class="row" v-if="addonsLoaded">
      <div class="col-4">
        <AddonList :addon-data="this.reactiveAddons"
                   :current-addon="this.currentAddon"
                   :current-filter="this.filter"
                   @addon-clicked="(addon) => addonClicked(addon)"
                   @change-sorting="(newSorting) => this.sorting = newSorting"
                   @filter-changed="(newFilter) => this.filter = newFilter"/>
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
