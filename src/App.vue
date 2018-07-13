<template lang="pug">
  .app
    Menu
    PostList
</template>

<script>
import Menu from './components/Menu'
import PostList from './components/PostList'
export default {
  name: 'App',
  components: {
    PostList,
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
