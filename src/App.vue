<script>
import AddonList from "@/components/AddonList.vue";
import AddonDetails from "@/components/AddonDetails.vue";
import HeaderBar from "@/components/HeaderBar.vue";

export default {
  data() {
    return {
      addonData: {},
      currentAddon: {},
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
        console.log(json)
        for (const addonKey in json) {
          json[addonKey]['name'] = addonKey;
        }
        this.addonData = json
        this.addonClicked(Object.keys(this.addonData)[0])
      })
    },
    addonClicked(addonKey) {
      this.currentAddon = this.addonData[addonKey]
    }
  },
  computed: {
    addonsLoaded() {
      return this.addonData !== undefined && Object.keys(this.addonData).length > 0;
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
        <AddonList :addon-data="this.addonData" :current-addon="this.currentAddon" @addon-clicked="(addon) => addonClicked(addon)"/>
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

<style>
.list {
  padding-top: 3.44rem;
}
</style>
