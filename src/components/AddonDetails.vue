<template>
  <div class="row">
    <h2>{{ addonDetails.name }}</h2>
  </div>
  <div class="row">
    <NumberDisplayWidget :values="numberDisplay"/>
  </div>
  <p>{{ addonDetails.versions }}</p>
</template>

<script>
import NumberDisplayWidget from "@/components/NumberDisplayWidget.vue";

export default {
  name: "AddonDetails",
  components: {NumberDisplayWidget},
  props: ["addonDetails"],
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
