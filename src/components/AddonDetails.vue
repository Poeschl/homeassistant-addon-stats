<template>
  <div class="col">
    <div class="row mb-2">
      <h2>{{ addonDetails.name }}</h2>
    </div>
    <div class="row mb-3">
      <NumberDisplayWidget :values="numberDisplay"/>
    </div>
    <div class="row mb-3">
      <VersionsChart :versions="addonDetails.versions"/>
    </div>
    <div class="row">
      <HistoryChart :versions="addonHistory"/>
    </div>
  </div>
</template>

<script>
import NumberDisplayWidget from "@/components/NumberDisplayWidget.vue";
import VersionsChart from "@/components/VersionsChart.vue";
import HistoryChart from "@/components/HistoryChart.vue";

export default {
  name: "AddonDetails",
  components: {HistoryChart, VersionsChart, NumberDisplayWidget},
  props: ["addonDetails","addonHistory"],
  computed: {
    numberDisplay() {
      return [
        {title: "Total Installations", value: this.addonDetails.total},
        {title: "Auto-Update enabled", value: this.addonDetails.auto_update},
        {title: "In protected environment", value: this.addonDetails.protected}
      ]
    }
  }
}
</script>

<style scoped>
.row {
  max-height: 500px;
}
</style>
