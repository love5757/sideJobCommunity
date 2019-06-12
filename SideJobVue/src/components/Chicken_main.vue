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
							<button @click="ShowDetailModal(i,idx)" class="item-btn detail">Detail</button>
						</div>
					</div>
				</div>
			</div>
		</div>
		<div class="modal hidden" ref="modal">
			<div class="modal__overlay"></div>
				<div class="item-container detail">
					<div class="item-header">
						<img :src="makeImage(detailIdx)" width="300" height="200" />
					</div>
					<div class="item-body">
						<div class="item-title">
							{{detailItem.title}}
						</div>
						<div class="item-content">
							<div style="text-align: center; height: 28px">
								{{detailItem.view}} <br> VIEW
							</div>
							<div class="item-content-detail more-detail">
								{{detailText}}
							</div>
							<div class="item-btn-wrap">
								<button @click="CloseDetailModal()" class="item-btn close">Close</button>
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
      img_src: '',
			detailItem: [],
			detailIdx: '',
			detailText: ''
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
		ShowDetailModal: function(item,idx) {
			const modal = this.$refs.modal;
			modal.classList.remove("hidden");
			let title = item.title!='미기재' ? `제목 : [${item.title}]\n`:''
			let type = item.types[0].type!='미기재' ? `타입 : ${item.types[0].type}\n`:''
			let email = item.writers[0].email!='미기재' ? `이메일 : ${item.writers[0].email}\n`:''
			let phone = item.writers[0].phone!='미기재' ? `전화번호 : ${item.writers[0].phone}\n`:''
			let kakaoId = item.writers[0].kakao_id!='미기재' ? `카카오ID : ${item.writers[0].kakao_id}\n`:''
			let kakaoName = item.writers[0].kakao_name!='미기재' ? `카카오대화명 : ${item.writers[0].kakao_name}\n`:''
			let fromHome = item.detail.from_home!='미기재' ? `재택여부 : ${item.detail.from_home}\n`:''
			let moreDetail = item.detail.more_detail!='미기재' ? `추가사항 : ${item.detail.more_detail}\n`:''
			let period = item.detail.period!='미기재' ? `기간 : ${item.detail.period }\n`:''
			let sector = item.detail.sector!='미기재' ? `분야 : ${item.detail.sector}\n`:''
			let skill = item.detail.skill!='미기재' ? `스킬 : ${item.detail.skill}\n`:''
			let stockOpt = item.detail.stock_opt!='미기재' ? `스톡옵션 : ${item.detail.stock_opt}\n`:''
			let url = item.detail.url!='미기재' ? `관련링크 : ${item.detail.url}\n`:''
			let years = item.detail.years!='미기재' ? `필요연차 : ${item.detail.years}\n`:''
			let location = item.companies[0].location!='미기재' ? `위치 : ${item.companies[0].location}\n`:''
			let name = item.companies[0].name!='미기재' ? `회사명 : ${item.companies[0].name}\n`:''

			this.detailText = name+ location+ sector+ email+ phone+ kakaoId+ kakaoName
												+ years+ skill+ period+ stockOpt+ fromHome+ url+ moreDetail
												+ `본문 : \n
												   ${item.content}`
			this.detailItem = item
			this.detailIdx = idx
		},
		CloseDetailModal: function() {
			const modal = this.$refs.modal;
			modal.classList.add("hidden");
		},
		makeImage: function(idx) {
			var index = (idx % 10)
			var img = require.context('../assets/img', false, /\.jpg$/)
			return img(`./${index}.jpg`)
		}
	}

}
</script>
