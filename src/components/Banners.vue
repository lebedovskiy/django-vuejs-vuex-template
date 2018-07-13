<template lang="pug">
  .banners
    .banner Hello!
    .banner Hello!
    .banner Hello!
</template>

<script>
export default {
  name: 'Banners'
}
</script>

<style lang="stylus">
.banners
  height 150px
  width 40%
  float right

.banner
  padding 0 10px
  width 25%
  float left
</style>
