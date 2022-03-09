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
      let retrievedData

      fetch("addons.json", {
        method: "GET",
        headers: {
          "Accept": "application/json"
        }
      })
          .then(response => {
            const data = response.json();
            console.log(JSON.stringify(data))
            return data
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
  computed: {
    addonsLoaded() {
      return this.addonData !== undefined && Object.keys(this.addonData) > 0;
    }
  },
  components: {
    HeaderBar,
    AddonList,
    AddonDetails,
  },
  beforeMount() {
    this.loadAddonData()
    if (this.addonData !== undefined) {
      this.addonClicked(Object.keys(this.addonData)[0])
    }
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
    <div class="row text-center" v-if="!addonsLoaded">
      <h3>No addon data available</h3>
    </div>
  </div>
</template>

<style>
.list {
  padding-top: 3.44rem;
}
</style>
