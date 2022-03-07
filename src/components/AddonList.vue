<template>
  <ul class="list-group">
    <li class="list-group-item"
        v-for="addon in addonData"
        :key="addon.name"
        @click="$emit('addonClicked', addon.name)"
        :class="{ active: addon.name === currentAddon.name }"
    >
      {{ addon.name }}
    </li>
  </ul>
</template>

<script>
export default {
  name: "AddonList",
  props: ["addonData", "currentAddon"],
}
</script>
