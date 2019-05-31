
export default {
  name: 'chickenMain',
  data () {
    return {
      items: [],
      img_src: 'http://www.urbanbrush.net/web/wp-content/uploads/edd/2018/02/web-20180211134119206041.png'
    }
  },
  created () {
    this.$axios.get('http://soorokim.duckdns.org:19223/getRecruitList')
      .then((response) => {
        console.log(response.data[0] + 'HELLLP')
        this.items = response.data
       // this.items['contents'].value = response.data['content'].substring(1, 2)
      })
  }
}
