<template lang="pug">
  .app
    .menu
      router-link.menu__item(to="/") Главная
      router-link.menu__item(to="/blog") Блог
      router-link.menu__item(to="/resume") Резюме
      router-link.menu__item(to="/write_me") Написать мне
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
    text-align left
    clear both

  a
    text-decoration none

  p
    line-height: 1.5

  .menu
    background black
    float none
    font-family Bahnschrift
    height 30px
    padding 1%
    @media (orientation: portrait)
      padding 2%
    max-width 100%
    opacity 0.5
    text-align center

  .menu__item
    font-size 1.5em
    @media (orientation: portrait)
      font-size 1.2em
    color white
    margin 0 1%

  .app
    -moz-osx-font-smoothing: grayscale
    -webkit-font-smoothing: antialiased
    background-color #ececec
    color: black
    font-family: 'Avenir', Helvetica, Arial, sans-serif
    float left

  footer
    background-color black
    color white
    font-family Bahnschrift
    opacity 0.75
    text-align center
</style>
