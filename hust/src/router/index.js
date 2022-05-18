import Vue from 'vue'
import VueRouter from 'vue-router'
import login from "../views/login.vue"
import user from '../views/user.vue'
import admin from '../views/admin.vue'
import goodlist from '../components/admin/shop_manage/admin_goods_list.vue'
import helplist from '../components/admin/help_manage/admin_help_list.vue'
import helprecordlist from '../components/admin/help_manage/admin_help_record_list.vue'
import shoprecordlist from '../components/admin/shop_manage/admin_shop_record_list.vue'
import userlist from '../components/admin/user_manage/admin_user_list.vue'
import situationcheck from '../components/admin/user_manage/admin_user_situation_check.vue'
import basicinformation from '../components/user/identiity/basicInformation.vue'
import certification from '../components/user/identiity/certification.vue'
import myshoptrade from '../components/user/identiity/myshop/myshop_trade.vue'
import myshopreview from '../components/user/identiity/myshop/myshop_review.vue'
import myshopgoods from '../components/user/identiity/myshop/myshop_goods.vue'
import myshopcollect from '../components/user/identiity/myshop/myshop_collect.vue'
import myshopbrowse from '../components/user/identiity/myshop/myshop_browse.vue'
import myhelptask from '../components/user/identiity/myhelp/myhelp_task.vue'
import myhelppublish from '../components/user/identiity/myhelp/myhelp_publish.vue'
import myhelpbrowse from '../components/user/identiity/myhelp/myhelp_browse.vue'
import goodask from '../components/user/shop/buy/goods_ask.vue'
import goodssearch from '../components/user/shop/buy/goods_search.vue'
import goodsmanage from '../components/user/shop/sell/goods_manage.vue'
import sellpublish from '../components/user/shop/sell/sell_publish.vue'
import helpneed from '../components/user/help/help_need.vue'
import helpoffer from '../components/user/help/help_offer.vue'
import register from '../views/register.vue'
Vue.use(VueRouter)

const routes = [
  // 默认加载路由为Index，无登录，就不需要登录界面
  {
    path: '/',
    component: login
  },{
    path: '/login',
    component: login
  },{
    path: '/user',
    component: user
  },{
    path: '/admin',
    component: admin
  },{
    path: '/goodlist',
    component: goodlist
  },{
    path: '/helplist',
    component: helplist
  },{
    path: '/helprecordlist',
    component: helprecordlist
  },{
    path: '/shoprecordlist',
    component: shoprecordlist
  },{
    path: '/userlist',
    component: userlist
  },{
    path: '/usersituationcheck',
    component: situationcheck
  },{
    path: '/basicinformation',
    component: basicinformation
  },{
    path: '/certification',
    component: certification
  },{
    path: '/myshoptrade',
    component: myshoptrade
  },{
    path: '/myshopreview',
    component: myshopreview
  },{
    path: '/myshopgoods',
    component: myshopgoods
  },{
    path: '/myshopcollect',
    component: myshopcollect
  },{
    path: '/myhopbrowse',
    component: myshopbrowse
  },{
    path: '/myhelptask',
    component: myhelptask
  },{
    path: '/myhelppublish',
    component: myhelppublish
  },{
    path: '/myhelpbrowse',
    component: myhelpbrowse
  },{
    path: '/goodask',
    component: goodask
  },{
    path: '/goodssearch',
    component: goodssearch
  },{
    path: '/goodsmanage',
    component: goodsmanage
  },{
    path: '/sellpublish',
    component: sellpublish
  },{
    path: '/helpneed',
    component: helpneed
  },{
    path: '/helpoffer',
    component: helpoffer
  },{
    path: '/register',
    component: register
  }
]

const router = new VueRouter({
  routes
})

export default router
