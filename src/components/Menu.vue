<template lang="pug">
    .header
        .logo
        a.menu__item menu item
        a.menu__item menu item
        a.menu__item menu item
        a.menu__item menu item
</template>

<script>
export default {
  name: 'Header'
}
</script>

<style lang="stylus">
.header
  text-align center
  background #1A01CC
  color white
  height 50px
  margin: 1em
  padding: 1em
  width: 90%

.logo
  width 50px
  height 50px
  float left

.menu__item
  float: left
  margin: 0 1em
</style>
