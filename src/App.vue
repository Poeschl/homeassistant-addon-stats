<script>
import AddonList from "@/components/AddonList.vue";
import AddonDetails from "@/components/AddonDetails.vue";

export default {
  data() {
    return {
      addonData: {},
      currentAddon: {},
    }
  },
  methods: {
    loadAddonData() {
      const retrievedData = {
        "a0d7b954_influxdb": {
          "total": 9371,
          "versions": {
            "4.1.0": 27,
            "4.3.0": 8533,
            "4.2.1": 429,
            "4.0.6": 51,
            "4.1.1": 198,
            "3.5.0": 1,
            "3.7.2": 2,
            "4.0.1": 17,
            "4.0.4": 22,
            "3.6.2": 2,
            "3.7.9": 15,
            "4.0.3": 52,
            "3.7.6": 2,
            "3.7.1": 3,
            "3.6.0": 2,
            "3.7.7": 4,
            "3.6.1": 1,
            "3.2.0": 1,
            "3.5.1": 2,
            "3.7.8": 1,
            "3.3.0": 1,
            "3.7.4": 2,
            "3.7.5": 2,
            "3.7.3": 1
          },
          "protected": 9366,
          "auto_update": 3843
        },
        "a0d7b954_ssh": {
          "total": 16689,
          "versions": {
            "8.2.2": 14,
            "10.0.2": 13450,
            "9.0.1": 752,
            "8.2.1": 97,
            "10.0.0": 584,
            "8.2.3": 71,
            "10.0.1": 662,
            "9.1.1": 528,
            "8.1.1": 44,
            "9.1.0": 87,
            "9.0.0": 173,
            "7.7.0": 3,
            "8.2.4": 89,
            "7.8.0": 17,
            "8.2.0": 39,
            "8.0.3": 21,
            "7.3.1": 2,
            "7.0.1": 2,
            "7.4.1": 5,
            "7.3.0": 5,
            "8.0.4": 6,
            "7.6.0": 7,
            "7.1.0": 1,
            "6.3.2": 1,
            "8.0.1": 10,
            "8.1.0": 6,
            "7.4.0": 3,
            "8.0.0": 3,
            "7.5.1": 1,
            "7.5.2": 1,
            "5.0.2": 1,
            "8.0.2": 1
          },
          "protected": 12880,
          "auto_update": 8383
        }
      }
      for (const addonKey in retrievedData) {
        retrievedData[addonKey]['name'] = addonKey;
      }
      this.addonData = retrievedData
    },
    addonClicked(addonKey) {
      this.currentAddon = this.addonData[addonKey]
      console.log("Loaded " + JSON.stringify(this.currentAddon))
    }
  },
  components: {
    AddonList,
    AddonDetails
  },
  mounted() {
    this.loadAddonData()
    this.addonClicked(Object.keys(this.addonData)[0])
  }
}
</script>

<template>
  <div>
    <AddonList :addon-data="this.addonData" @addon-clicked="(addon) => addonClicked(addon)"/>
    <br/>
    <AddonDetails :addon-details="currentAddon"/>
  </div>
</template>

<style>

</style>
