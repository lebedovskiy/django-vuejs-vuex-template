<template lang="pug">
  .app
    .header
      .nav
    router-view
    footer.footer Powered by Lebedoskiy, 2018
</template>

<script>
export default {
  name: 'App'
}
</script>

<style lang="stylus">
  body
    margin 0

  .app
    -moz-osx-font-smoothing: grayscale
    -webkit-font-smoothing: antialiased
    background-color #ececec
    color: #2c3e50
    font-family: 'Avenir', Helvetica, Arial, sans-serif

  .nav
    background-color #0c5aa6
    height 50px
    opacity 0.75
    width 100%

  footer
    background-color #0c5aa6bf
    color #000000
    font-family Bahnschrift
    text-align center
</style>
