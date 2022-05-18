<template>
  <div class="index">
    <el-dialog
      title="注册"
      :visible.sync="dialogVisible"
      width="30%"
      @close="closeDialog"
    >
      <reg></reg>
      <span slot="footer" class="dialog-footer">
        <el-button @click="dialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="dialogVisible = false"
          >确 定</el-button
        >
      </span>
    </el-dialog>
    <div class="head">
      <div class="title">Hust帮</div>
    </div>
    <div class="content">
      <el-tabs v-model="activeName" type="border-card" @tab-click="handleClick">
        <el-tab-pane label="用户登录" name="user">
          <el-form
            :model="ruleForm"
            :rules="rules"
            ref="ruleForm"
            label-width="100px"
            class="demo-ruleForm"
          >
            <el-form-item label="用户名" prop="username">
              <el-input v-model="ruleForm.username"></el-input>
            </el-form-item>
            <el-form-item label="密码" prop="password">
              <el-input v-model="ruleForm.password" show-password></el-input>
            </el-form-item>
            <el-form-item>
              <el-button type="primary" @click="userLogin()">登陆</el-button>
              <el-button @click="dialogVisible = true">注册</el-button>
            </el-form-item>
          </el-form>
        </el-tab-pane>
        <el-tab-pane label="管理员登陆" name="admin">
          <el-form
            :model="ruleForm"
            :rules="rules"
            ref="ruleForm"
            label-width="100px"
            class="demo-ruleForm"
          >
            <el-form-item label="用户名" prop="username">
              <el-input v-model="ruleForm.username"></el-input>
            </el-form-item>
            <el-form-item label="密码" prop="password">
              <el-input v-model="ruleForm.password" show-password></el-input>
            </el-form-item>
            <el-form-item>
              <el-button type="primary" @click="adminLogin()">登陆</el-button>
            </el-form-item>
          </el-form>
        </el-tab-pane>
      </el-tabs>
    </div>
    <div class="foot">
      <div style="padding-left: 80%">© 2021　建设信息系统开发课程 第六组</div>
    </div>
  </div>
</template>

<script>
import reg from "../views/register.vue";
export default {
  data() {
    return {
      activeName: "user",
      ruleForm: {
        username: "",
        password: "",
      },
      dialogVisible: false,
      rules: {
        username: [
          { required: true, message: "请输入用户名", trigger: "blur" },
        ],
        password: [{ required: true, message: "请输入密码", trigger: "blur" }],
      },
    };
  },
  components: {
    reg: reg,
  },
  methods: {
    handleClick(tab, event) {
      console.log(tab, event);
    },
    userLogin() {
      if (this.ruleForm.username == "") {
        alert("请输入用户名！");
      } else if (this.ruleForm.password == "") {
        alert("请输入密码！");
      } else {
        $.ajax({
          type: "get", //请求方式,默认值GET
          data: {
            username: this.ruleForm.username,
            password: this.ruleForm.password,
          }, //请求参数，自动转换为字符串格式，如果是get请求，会自动拼接到url上面
          url: "http://218.197.209.26:8081/userlogin", //请求地址
          context: document.body, //绑定回调中的this
          jsonp: "callback", //在一个jsonp请求中重写回调函数的名字。
          //规定预期的服务器响应的数据类型。默认执行智能判断（xml、json、script 或 html）。
          contentType: "application/x-www-form-urlencoded", //发送数据至服务器内容编码类型
          success: function (data) {
            alert(data);
            if (data == "登陆成功！") {
              window.location.href = "http://localhost:8080#/user";
            }
          },
        });
      }
    },
    adminLogin() {
      if (this.ruleForm.username == "") {
        alert("请输入用户名！");
      } else if (this.ruleForm.password == "") {
        alert("请输入密码！");
      } else {
        $.ajax({
          type: "get", //请求方式,默认值GET
          data: {
            username: this.ruleForm.username,
            password: this.ruleForm.password,
          }, //请求参数，自动转换为字符串格式，如果是get请求，会自动拼接到url上面
          url: "http://218.197.209.26:8081/adminlogin", //请求地址
          context: document.body, //绑定回调中的this
          jsonp: "callback", //在一个jsonp请求中重写回调函数的名字。
          //规定预期的服务器响应的数据类型。默认执行智能判断（xml、json、script 或 html）。
          contentType: "application/x-www-form-urlencoded", //发送数据至服务器内容编码类型
          success: function (data) {
            alert(data);
            if (data == "登陆成功！") {
              window.location.href = "http://localhost:8080/#/admin";
            }
          },
        });
      }
    },
    closeDialog() {
      this.dialogVisible = false;
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

.content {
  position: relative;
  float: left;
  height: 800px;
  width: 90%;
}
.foot {
  position: absolute;
  bottom: 0;
  width: 99%;
}
.content {
  width: 500px;
  position: absolute;
  top: 40%;
  left: 37%;
}
</style>