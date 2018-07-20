<template lang="pug">
.resume
    .header
      h3.header__title {{resume.title}}
        .header__phone Телефон: {{resume.phone}}
        .header__email Эл. почта: {{resume.e_mail}}
      img.resume__img(width='100%', src='../assets/resume__img.jpg')
    p.resume__salary Ожидаемая зарплата: {{resume.salary}}
    p.resume__education Образование: {{resume.education}}
    p.resume__language Владение языками: {{resume.language}}
    p.resume__stack Стек: {{resume.stack}}
    p.resume__skills Навыки: {{resume.skills}}
    p.resume__text О себе: {{resume.text}}
    p.resume__link Ссылка на моё резюме на HeadHunter:
      a(href="https://chelyabinsk.hh.ru/resume/1f2a6d5bff058f24550039ed1f453753373559") https://chelyabinsk.hh.ru/resume/1f2a6d5bff058f24550039ed1f453753373559
</template>

<script>
import {HTTP} from '../api/common'
export default {
  name: 'Resume',
  data () {
    return {
      resume: []
    }
  },
  mounted () {
    HTTP
      .get('presentation')
      .then(response => (this.resume = response.data[0]))
  }
}
</script>

<style lang="stylus">
  .resume
    width 60%
    margin 0 auto
    overflow auto
    @media screen and (max-width: 996px)
      width 95%

  .header
    margin 1em 0
    overflow auto

 .header__title
   line-height 1.5
   overflow auto
   @media screen and (orientation: landscape)
    float left
    margin 1% 0
    width 49%

 .header__phone
   float none

  .resume__img
    @media screen and (orientation: landscape)
      float right
      width 49%

  .resume__text
    width 95%
    line-height 1.2
</style>
