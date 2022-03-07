<script>
import AddonList from "@/components/AddonList.vue";
import AddonDetails from "@/components/AddonDetails.vue";
import Header from "@/components/HeaderBar.vue";

export default {
  data() {
    return {
      addonData: {},
      currentAddon: {},
    }
  },
  methods: {
    loadAddonData() {
      let retrievedData

      fetch("https://analytics.home-assistant.io/addons.json", {mode: "no-cors", method: "GET"})
          .then(response => {
            console.log(JSON.stringify(response))
            response.json()
          })
          .then(data => retrievedData = data)
          .catch(error => {
            console.error("Error on retrieving data", error)
          })

      for (const addonKey in retrievedData) {
        retrievedData[addonKey]['name'] = addonKey;
      }
      this.addonData = retrievedData
    },
    addonClicked(addonKey) {
      this.currentAddon = this.addonData[addonKey]
    }
  },
  components: {
    Header,
    AddonList,
    AddonDetails,
  },
  beforeMount() {
    this.loadAddonData()
    this.addonClicked(Object.keys(this.addonData)[0])
  }
}
</script>

<template>
  <Header/>
  <div class="container">
    <div class="row">
      <div class="col-4 list">
        <AddonList :addon-data="this.addonData" :current-addon="this.currentAddon" @addon-clicked="(addon) => addonClicked(addon)"/>
      </div>
      <div class="col-8">
        <AddonDetails :addon-details="this.currentAddon"/>
      </div>
    </div>
  </div>
</template>

<style>
.list {
  padding-top: 3.44rem;
}
</style>
