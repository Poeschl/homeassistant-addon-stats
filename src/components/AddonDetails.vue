<template>
  <p>{{ addonDetails.name }}</p>
  <p>{{ addonDetails.total }}</p>
  <p>{{ addonDetails.versions }}</p>
  <p>{{ addonDetails.protected }}</p>
  <p>{{ addonDetails.auto_update }}</p>
</template>

<script>
export default {
  name: "AddonDetails",
  props: ["addonDetails"],
}
</script>
