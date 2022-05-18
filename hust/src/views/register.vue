<template>
  <div class="register">
    <el-form
      :model="ruleForm"
      :rules="rules"
      ref="ruleForm"
      label-width="120px"
      class="demo-ruleForm"
    >
      <el-form-item label="用户名" prop="username">
        <el-input v-model="ruleForm.username"></el-input>
      </el-form-item>
      <el-form-item label="密码" prop="password">
        <el-input v-model="ruleForm.password" show-password></el-input>
      </el-form-item>
      <el-form-item label="再次输入密码" prop="passwords">
        <el-input v-model="ruleForm.passwords" show-password></el-input>
      </el-form-item>
      <el-form-item label="姓名" prop="name">
        <el-input v-model="ruleForm.name"></el-input>
      </el-form-item>
      <el-form-item label="性别" prop="sex">
        <el-select v-model="ruleForm.sex" placeholder="请选择性别">
          <el-option label="男" value="男"></el-option>
          <el-option label="女" value="女"></el-option>
        </el-select>
      </el-form-item>
      <el-form-item label="出生日期" required>
        <el-form-item prop="birthdate">
          <el-date-picker
            type="date"
            placeholder="选择日期"
            v-model="ruleForm.birthdate"
            style="width: 100%"
          ></el-date-picker>
        </el-form-item>
      </el-form-item>
      <el-form-item label="学号" prop="snumber">
        <el-input v-model="ruleForm.snumber"></el-input>
      </el-form-item>
      <el-form-item label="学院" prop="college">
        <el-input v-model="ruleForm.college"></el-input>
      </el-form-item>
      <el-form-item label="专业" prop="academy">
        <el-input v-model="ruleForm.academy"></el-input>
      </el-form-item>
      <el-form-item label="班级" prop="class">
        <el-input v-model="ruleForm.class"></el-input>
      </el-form-item>
      <el-form-item label="QQ号" prop="qqnum">
        <el-input v-model="ruleForm.qqnum"></el-input>
      </el-form-item>
      <el-form-item label="联系方式" prop="contact">
        <el-input v-model="ruleForm.contact"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="register">注册</el-button>
        <el-button @click="resetForm('ruleForm')">重置</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
export default {
  data() {
    var validatePass = (rule, value, callback) => {
      if (value === "") {
        callback(new Error("请再次输入密码"));
      } else if (value !== this.ruleForm.password) {
        callback(new Error("两次输入密码不一致!"));
      } else {
        callback();
      }
    };
    return {
      ruleForm: {
        username: "",
        password: "",
        passwords: "",
        name: "",
        sex: "",
        birthdate: "",
        snumber: "",
        college: "",
        academy: "",
        class: "",
        qqnum: "",
        contact: "",
      },
      rules: {
        name: [{ required: true, message: "请输入姓名", trigger: "blur" }],
        username: [
          { required: true, message: "请输入用户名", trigger: "blur" },
        ],
        password: [{ required: true, message: "请输入密码", trigger: "blur" }],
        passwords: [
          { required: true, validator: validatePass, trigger: "blur" },
        ],
        snumber: [{ required: true, message: "请输入学号", trigger: "blur" }],
        college: [{ required: true, message: "请输入学院", trigger: "blur" }],
        academy: [{ required: true, message: "请输入专业", trigger: "blur" }],
        class: [{ required: true, message: "请输入班级", trigger: "blur" }],
        qqnum: [{ required: true, message: "请输入QQ号", trigger: "blur" }],
        contact: [
          { required: true, message: "请输入联系方式", trigger: "blur" },
        ],
        sex: [{ required: true, message: "请选择性别", trigger: "change" }],
        birthdate: [
          {
            type: "date",
            required: true,
            message: "请选择日期",
            trigger: "change",
          },
        ],
      },
    };
  },

  methods: {
    register() {
      if (this.ruleForm.username == "") {
        alert("请输入用户名！");
      } else if (this.ruleForm.password == "") {
        alert("请输入密码！");
      } else if (this.ruleForm.passwords == "") {
        alert("请再次输入密码！");
      } else if (this.ruleForm.name == "") {
        alert("请输入姓名！");
      } else if (this.ruleForm.sex == "") {
        alert("请选择性别！");
      } else if (this.ruleForm.birthdate == "") {
        alert("请选择生日！");
      } else if (this.ruleForm.snumber == "") {
        alert("请输入学号！");
      } else if (this.ruleForm.college == "") {
        alert("请输入学院！");
      } else if (this.ruleForm.academy == "") {
        alert("请输入专业！");
      } else if (this.ruleForm.class == "") {
        alert("请输入班级！");
      } else if (this.ruleForm.qqnum == "") {
        alert("请输入QQ号！");
      } else if (this.ruleForm.contact == "") {
        alert("请输入联系方式！");
      } else {
        $.ajax({
          type: "get", //请求方式,默认值GET
          data: {
            username: this.ruleForm.username,
            password: this.ruleForm.password,
            name: this.ruleForm.name,
            sex: this.ruleForm.sex,
            birthdate: this.ruleForm.birthdate,
            snumber: this.ruleForm.snumber,
            college: this.ruleForm.college,
            academy: this.ruleForm.academy,
            class: this.ruleForm.class,
            qqnum: this.ruleForm.qqnum,
            contact: this.ruleForm.contact,
          }, //请求参数，自动转换为字符串格式，如果是get请求，会自动拼接到url上面
          url: "http://218.197.209.26:8081/register", //请求地址
          context: document.body, //绑定回调中的this
          jsonp: "callback", //在一个jsonp请求中重写回调函数的名字。
          //规定预期的服务器响应的数据类型。默认执行智能判断（xml、json、script 或 html）。
          contentType: "application/x-www-form-urlencoded", //发送数据至服务器内容编码类型
          success: function (data) {
            alert(data);
          },
        });
      }
    },
    resetForm(formName) {
      this.$refs[formName].resetFields();
    },
  },
};
</script>

<style>
</style>