<template>
  <div>
    <div v-for="(addon, addonKey) in addonData" :key="addonKey" @click="$emit('addonClicked', addonKey)">
      <h2>{{ addonKey }}</h2>
    </div>
  </div>
</template>

<script>
export default {
  name: "AddonList",
  props: ["addonData"],
}
</script>
