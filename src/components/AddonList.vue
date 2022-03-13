<template>
  <div class="mb-3 d-flex justify-content-between">
    <div class=""></div>
    <div class="dropdown">
      <button class="btn btn-secondary dropdown-toggle" type="button" id="sortingButton" data-bs-toggle="dropdown" aria-expanded="false">
        Addon Sorting
      </button>
      <ul class="dropdown-menu dropdown-menu-end" aria-labelledby="sortingButton">
        <li @click="$emit('changeSorting', 'name')">
          <a class="dropdown-item" href="#">Name</a>
        </li>
        <li @click="$emit('changeSorting', 'total')">
          <a class="dropdown-item" href="#">Total Installations</a>
        </li>
      </ul>
    </div>
  </div>
  <div class="list-scroll overflow-auto">
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
  </div>
</template>

<script>
export default {
  name: "AddonList",
  props: ["addonData", "currentAddon"],
  emits: ["changeSorting", "addonClicked"]
}
</script>

<style>
.list-scroll {
  height: 80vh;
}
</style>
