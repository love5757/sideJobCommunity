<template>
	<div id="app" style="text-align: center;">
		<div class="container" v-for="(i,idx) in items" :key="i.id">
			<div class="item-container">
				<div class="item-header">
					<img :src="makeImage(idx)" width="300" height="200" />
				</div>
				<div class="item-body">
					<div class="item-title"> 
						{{i.title}}
					</div>
					<div class="item-content">
						<div style="text-align: center; height: 28px">
							{{i.view}} <br> VIEW
						</div>
						<div class="item-content-detail">
							{{i.content}}	
						</div>
						<div class="item-btn-wrap">
							<button @click="viewCount(i.recr_id)" class="item-btn">Detail</button>
						</div>
					</div>
				</div>
			</div>	
		</div>
	</div>
</template>

<script>
import { eventBus } from '../main';

export default {
  name: 'chickenMain',
  data: function () {
    return {
			items: [],
			images : ['@/assets/img/1.jpg','@/assets/img/2.jpg','@/assets/img/3.jpg','@/assets/img/4.jpg','@/assets/img/5.jpg',
			'@/assets/img/6.jpg','@/assets/img/7.jpg', '@/assets/img/8.jpg', '@/assets/img/9.jpg', '@/assets/img/10.jpg'],
      img_src: ''
    }
  },
  created () {
    this.$axios.get('http://soorokim.duckdns.org:19223/getRecruitList')
      .then((response) => {
				this.items = response.data
				eventBus.$emit('listChange', this.items.length);
			})
  },
  methods: {
		viewCount: function(id) {
			console.log(id);
		}, 
		makeImage: function(idx) {
			var index = (idx % 10)
			var img = require.context('../assets/img', false, /\.jpg$/)
			console.log(img('./' + index + ".jpg" ))
			return img('./' + index + ".jpg" )
		}

		
	}
	
}
</script>