<template lang="pug">
  .app
    Menu
    right-side
    left-side
</template>

<script>
import Menu from './components/Menu'
import LeftSide from './components/LeftSide'
import RightSide from './components/RightSide'
export default {
  name: 'App',
  components: {
    RightSide,
    LeftSide,
    Menu
  }
}
</script>

<style lang="stylus">
.app
  font-family: 'Avenir', Helvetica, Arial, sans-serif
  -webkit-font-smoothing: antialiased
  -moz-osx-font-smoothing: grayscale
  color: #2c3e50
</style>
