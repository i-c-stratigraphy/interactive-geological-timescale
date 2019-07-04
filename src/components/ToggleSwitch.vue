<template>
  <div id="switch">
    <div id='label' v-if="label">{{label}}</div>
    <ul>
        <li v-for='(value, index) in values' v-bind:key="index" @click="selectItem(value)" :class="(value == selectedItem) ? 'selected' : 'not-selected'">{{value}}</li>
    </ul>
  </div>
</template>

<script>

export default {
  name: 'ToggleSwitch',
  props: {
      values: Array,
      label: {
          type: String,
          default: null
      },
      defaultSelected: {
          type: String,
          default: null
      }
  },
  methods: {
      selectItem: function(item){
          this.selectedItem = item
          this.$emit('input', item)
      }
  },
  data() {
      return{
        selectedItem: this.defaultSelected
      }
  }
}
</script>

<style scoped>
.not-selected{
    opacity: 0.25;
    transition: opacity 0.5s;
}
.selected{
    transition: opacity 0.5s;
}
ul{
    margin-left: auto;
    margin-right: auto;
    text-align: center;
}
li{
    color: #2C3E50;
    font-weight: bold;
    cursor: pointer;
    font-size: 1.4em;
    position: relative;
    width: 150px;
    text-align: center;
}
#label {
    font-weight: 400;
    font-size: 1.2em;
}
</style>
