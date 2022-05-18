<template>
  <div class="basic_info">
      <div class="aside1">
    <img src="../../../assets/picture/我的.png" alt="">
  </div>
      <div class="aside2">
    <p style="padding-left:20px;">基本信息</p>
    <hr>
    <div style="margin-top: 5%;">
      <div style="float: left;width: 33.3%;">
        <div style="text-align: center;">
          <div style="float: left; width: 35%;text-align: right;">学号</div>
          <div style="float: left;">
            <form>
              <input v-model="user_info[0].snumber" type="text" name="number" >
            </form>
          </div>
        </div>
      </div>
      <div style="float: left;width: 33.3%;">
        <div style="text-align: center;">
          <div style="float: left; width: 35%;text-align: right;">姓名</div>
          <div style="float: left;">
            <form>
              <input v-model="user_info[0].name" type="text" name="name">
            </form>
          </div>
        </div>
      </div>
      <div style="float: left;width: 33.3%;">
        <div style="text-align: center;">
          <div style="float: left; width: 35%;text-align: right;">性别</div>
          <div style="float: left;">
            <form>
              <input type="text" name="sex" >
            </form>
          </div>
        </div>
      </div>
      <br>
      <div style="float: left;width: 33.3%;margin-top: 5%;">
        <div style="text-align: center;">
          <div style="float: left; width: 35%;text-align: right;">学院</div>
          <div style="float: left;">
            <form>
              <input v-model="user_info[0].college" type="text" name="college">
            </form>
          </div>
        </div>
      </div>
      <div style="float: left;width: 33.3%;margin-top: 5%;">
        <div style="text-align: center;">
          <div style="float: left; width: 35%;text-align: right;">专业</div>
          <div style="float: left;">
            <form>
              <input v-model="user_info[0].academy" type="text" name="major">
            </form>
          </div>
        </div>
      </div>
      <div style="float: left;width: 33.3%;margin-top: 5%;">
        <div style="text-align: center;">
          <div style="float: left; width: 35%;text-align: right;">班级</div>
          <div style="float: left;">
            <form>
              <input v-model="user_info[0].class" type="text" name="class">
            </form>
          </div>
        </div>
      </div>
      <br>
      <div style="float: left;width: 33.3%;margin-top: 5%;">
        <div style="text-align: center;">
          <div style="float: left; width: 35%;text-align: right;">出生日期</div>
          <div style="float: left;">
            <form>
              <input v-model="user_info[0].birthdate" type="text" name="birth">
            </form>
          </div>
        </div>
      </div>
      <div style="float: left;width: 33.3%;margin-top: 5%;">
        <div style="text-align: center;">
          <div style="float: left; width: 35%;text-align: right;">QQ</div>
          <div style="float: left;">
            <form>
              <input v-model="user_info[0].qqnum" type="text" name="QQ">
            </form>
          </div>
        </div>
      </div>
      <div style="float: left;width: 33.3%;margin-top: 5%;">
        <div style="text-align: center;">
          <div style="float: left; width: 35%;text-align: right;">联系电话</div>
          <div style="float: left;">
            <form>
              <input v-model="user_info[0].contact" type="text" name="tel" maxlength="11">
            </form>
          </div>
        </div>
      </div>
    </div>
    <button style="margin-left:50%;margin-top:5%">
      确定
    </button>
  </div>
  </div>
</template>

<script>
export default {
  data(){
    return{
      user_info: [],
    }
  },
  mounted() {
    this.getdata();
  },
  methods: {
    getdata() {
      var that = this;
      $.ajax({
        type: "get", //请求方式,默认值GET
        data: "", //请求参数，自动转换为字符串格式，如果是get请求，会自动拼接到url上面
        url: "http://218.197.209.26:8081/data", //请求地址
        context: document.body, //绑定回调中的this
        async: true, //是否是异步请求，默认情况下都是true,如果要发送同步请求，则改为false
        cache: false, //是否返回此页面，默认值为true
        dataType: "json",
        jsonp: "callback", //在一个jsonp请求中重写回调函数的名字。
        //规定预期的服务器响应的数据类型。默认执行智能判断（xml、json、script 或 html）。
        contentType: "application/x-www-form-urlencoded", //发送数据至服务器内容编码类型
        success: function (data) {
          that.user_info = data.user_info;
        },
      });
    },
  },
};
</script>

<style scoped>
.aside1 {
  margin: 2% 2%;
  background-color: lightgray;
  float: left;
  width: 12%;
  height: 600px;
  text-align: center;
}

.aside2 {
  margin: 2% 2%;
  background-color: lightgrey;
  color: rgb(0, 0, 0);
  float: right;
  width: 80%;
  height: 600px;
}
</style>