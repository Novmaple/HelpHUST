<template>
  <div class="index">
    <div class="head">
      <div class="title">Hust帮</div>
      <div class="welcome">欢迎您，管理员张三！</div>
      <div class="return">
        <a href="http://localhost:8080/#/login">
          <el-button size="mini">退出登陆</el-button>
        </a>
      </div>
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
              <span>用户管理</span>
            </template>
            <el-menu-item-group>
              <el-menu-item index="1-1" @click="changePage(1)"
                >用户列表</el-menu-item
              >
              <el-menu-item index="1-2" @click="changePage(2)"
                >资质认证审核</el-menu-item
              >
            </el-menu-item-group>
          </el-submenu>
          <el-submenu index="2">
            <template slot="title">
              <i class="el-icon-s-shop"></i>
              <span>市场管理</span>
            </template>
            <el-menu-item-group>
              <el-menu-item index="2-1" @click="changePage(3)"
                >商品列表</el-menu-item
              >
              <el-menu-item index="2-2" @click="changePage(4)"
                >记录列表</el-menu-item
              >
            </el-menu-item-group>
          </el-submenu>
          <el-submenu index="3">
            <template slot="title">
              <i class="el-icon-s-help"></i>
              <span>互助管理</span>
            </template>
            <el-menu-item-group>
              <el-menu-item index="3-1" @click="changePage(5)"
                >互助信息列表</el-menu-item
              >
              <el-menu-item index="3-2" @click="changePage(6)"
                >记录列表</el-menu-item
              >
            </el-menu-item-group>
          </el-submenu>
        </el-menu>
      </el-col>
    </div>
    <div class="content">
      <userlist v-show="show == 1"></userlist>
      <usercheck v-show="show == 2"></usercheck>
      <goodlist v-show="show == 3"></goodlist>
      <shoprecordlist v-show="show == 4"></shoprecordlist>
      <helplist v-show="show == 5"></helplist>
      <helprecordlist v-show="show == 6"></helprecordlist>
    </div>
    <div class="foot">
      <div style="padding-left: 80%">© 2021　建设信息系统开发课程 第六组</div>
    </div>
  </div>
</template>

<script>
import userlist from '../components/admin/user_manage/admin_user_list.vue';
import usercheck from '../components/admin/user_manage/admin_user_situation_check.vue';
import goodlist from '../components/admin/shop_manage/admin_goods_list.vue';
import shoprecordlist from '../components/admin/shop_manage/admin_shop_record_list.vue';
import helplist from '../components/admin/help_manage/admin_help_list.vue';
import helprecordlist from '../components/admin/help_manage/admin_help_record_list.vue';
export default {
  data() {
    return {
      show: 1,
    };
  },
  components: {
    userlist: userlist,
    usercheck: usercheck,
    goodlist: goodlist,
    shoprecordlist: shoprecordlist,
    helplist: helplist,
    helprecordlist: helprecordlist,
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
.title {
  width: 20%;
  height: 20%;
  font-size: 50px;
  padding-left: 5%;
  padding-top: 0.8%;
}
.return{
  position:absolute;
  right:1%;
  top:45%;
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
  margin-top: 2%;
  height: 800px;
  width: 89%;
}
.foot {
  position: absolute;
  bottom: 0;
  width: 99%;
}
</style>