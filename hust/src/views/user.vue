<template>
  <div class="index">
    <div class="head">
      <div class="title">Hust帮</div>
      <div class="welcome">欢迎您，用户刘一！</div>
      <div class="return">
        <a href="http://localhost:8080/#/login">
          <el-button size="mini">退出登陆</el-button>
        </a>
      </div>
      <div class="check" style="color: green">您已通过本年度资质认证！</div>
    </div>
    <div class="navigation">
      <el-col :span="12">
        <el-menu
          default-active="2"
          class="el-menu-vertical-demo"
          @open="handleOpen"
          @close="handleClose"
          :unique-opened="true"
        >
          <el-submenu index="1">
            <template slot="title">
              <i class="el-icon-user-solid"></i>
              <span>个人用户</span>
            </template>
            <el-menu-item-group>
              <el-menu-item index="1-1" @click="changePage(1)">基本信息</el-menu-item>
              <el-menu-item index="1-2" @click="changePage(2)">资质认证</el-menu-item>
            </el-menu-item-group>
            <el-submenu index="1-3">
              <template slot="title">我的市场</template>
              <el-menu-item index="1-3-1" @click="changePage(3)">浏览记录</el-menu-item>
              <el-menu-item index="1-3-2" @click="changePage(4)">我的收藏</el-menu-item>
              <el-menu-item index="1-3-3" @click="changePage(5)">交易记录</el-menu-item>
              <el-menu-item index="1-3-4" @click="changePage(6)">我的商品</el-menu-item>
              <el-menu-item index="1-3-5" @click="changePage(7)">我的评价</el-menu-item>
            </el-submenu>
            <el-submenu index="1-4">
              <template slot="title">我的互助</template>
              <el-menu-item index="1-4-1" @click="changePage(8)">浏览记录</el-menu-item>
              <el-menu-item index="1-4-2" @click="changePage(9)">我的发布</el-menu-item>
              <el-menu-item index="1-4-3" @click="changePage(10)">我的任务</el-menu-item>
            </el-submenu>
          </el-submenu>
          <el-submenu index="2">
            <template slot="title">
              <i class="el-icon-s-shop"></i>
              <span>交易市场</span>
            </template>
            <el-submenu index="2-1">
              <template slot="title">我要买</template>
              <el-menu-item index="2-1-1" @click="changePage(11)">商品查询</el-menu-item>
              <el-menu-item index="2-1-2" @click="changePage(12)">需求发布</el-menu-item>
            </el-submenu>
            <el-submenu index="2-2">
              <template slot="title">我要卖</template>
              <el-menu-item index="2-2-1" @click="changePage(13)">我要发布</el-menu-item>
              <el-menu-item index="2-2-2" @click="changePage(14)">商品管理</el-menu-item>
            </el-submenu>
          </el-submenu>
          <el-submenu index="3">
            <template slot="title">
              <i class="el-icon-s-help"></i>
              <span>校园互助</span>
            </template>
            <el-menu-item-group>
              <el-menu-item index="3-1" @click="changePage(15)">我需要帮助</el-menu-item>
              <el-menu-item index="3-2" @click="changePage(16)">我提供帮助</el-menu-item>
            </el-menu-item-group>
          </el-submenu>
        </el-menu>
      </el-col>
    </div>
    <div class="content">
      <basicinformation v-show="show == 1"></basicinformation>
      <certification v-show="show == 2"></certification>
      <myshopbrowse v-show="show == 3"></myshopbrowse>
      <myshopcollect v-show="show == 4"></myshopcollect>
      <myshoptrade v-show="show == 5"></myshoptrade>
      <myshopgoods v-show="show == 6"></myshopgoods>
      <myshopreview v-show="show == 7"></myshopreview>
      <myhelpbrowse v-show="show == 8"></myhelpbrowse>
      <myhelppublish v-show="show == 9"></myhelppublish>
      <myhelptask v-show="show == 10"></myhelptask>
      <goodssearch v-show="show == 11"></goodssearch>
      <goodask v-show="show == 12"></goodask>
      <sellpublish v-show="show == 13"></sellpublish>
      <goodsmanage v-show="show == 14"></goodsmanage>
      <helpneed v-show="show == 15"></helpneed>
      <helpoffer v-show="show == 16"></helpoffer>
    </div>
    <div class="foot">
      <div style="padding-left: 80%">© 2021　建设信息系统开发课程 第六组</div>
    </div>
  </div>
</template>

<script>
import basicinformation from "../components/user/identiity/basicInformation.vue";
import certification from "../components/user/identiity/certification.vue";
import myshoptrade from "../components/user/identiity/myshop/myshop_trade.vue";
import myshopreview from "../components/user/identiity/myshop/myshop_review.vue";
import myshopgoods from "../components/user/identiity/myshop/myshop_goods.vue";
import myshopcollect from "../components/user/identiity/myshop/myshop_collect.vue";
import myshopbrowse from "../components/user/identiity/myshop/myshop_browse.vue";
import myhelptask from "../components/user/identiity/myhelp/myhelp_task.vue";
import myhelppublish from "../components/user/identiity/myhelp/myhelp_publish.vue";
import myhelpbrowse from "../components/user/identiity/myhelp/myhelp_browse.vue";
import goodask from "../components/user/shop/buy/goods_ask.vue";
import goodssearch from "../components/user/shop/buy/goods_search.vue";
import goodsmanage from "../components/user/shop/sell/goods_manage.vue";
import sellpublish from "../components/user/shop/sell/sell_publish.vue";
import helpneed from "../components/user/help/help_need.vue";
import helpoffer from "../components/user/help/help_offer.vue";
export default {
  data() {
    return {
      show: 1,
    };
  },
  components: {
    basicinformation: basicinformation,
    certification: certification,
    myshoptrade: myshoptrade,
    myshopreview: myshopreview,
    myshopgoods: myshopgoods,
    myshopcollect: myshopcollect,
    myshopbrowse: myshopbrowse,
    myhelptask: myhelptask,
    myhelppublish: myhelppublish,
    myhelpbrowse: myhelpbrowse,
    goodask: goodask,
    goodssearch: goodssearch,
    goodsmanage: goodsmanage,
    sellpublish: sellpublish,
    helpneed: helpneed,
    helpoffer: helpoffer,
  },
  methods: {
    changePage(p) {
      this.show = p;
    },
  },
};
</script>

<style scoped>
.head {
  background-color: aqua;
  height: 100px;
  position: relative;
}
.welcome {
  position: relative;
  padding-top: 0.6%;
  padding-left: 85%;
}
.check {
  position: relative;
  padding-left: 84%;
}
.title {
  width: 20%;
  height: 20%;
  font-size: 50px;
  padding-left: 5%;
  padding-top: 0.8%;
}
.return {
  position: absolute;
  right: 1%;
  top: 45%;
}
.navigation {
  position: relative;
  float: left;
  width: 11%;
  height: 800px;
}
.content {
  position: relative;
  float: left;
  height: 800px;
  width: 89%;
  margin-top:2%
}
.foot {
  position: absolute;
  bottom: 0;
  width: 99%;
}
</style>