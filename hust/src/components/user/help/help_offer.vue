<template>
  <div class="myhelp_publish">
    <div style="background-color: lightgray; width: 100%; height: 600px">
      <p style="padding-top: 20px; padding-left: 20px">我的帮助</p>
      <hr />
      <table>
        <td>
          <input
            type="button"
            value="已发布"
            style="
              width: 100%;
              height: 100%;
              background-color: rgb(255, 255, 255);
            "
          />
        </td>
        <td>
          <input
            type="button"
            value="已接受"
            style="
              width: 100%;
              height: 100%;
              background-color: rgb(255, 255, 255);
            "
          />
        </td>
        <td>
          <input
            type="button"
            value="未付款"
            style="
              width: 100%;
              height: 100%;
              background-color: rgb(255, 255, 255);
            "
          />
        </td>
        <td>
          <input
            type="button"
            value="已付款"
            style="
              width: 100%;
              height: 100%;
              background-color: rgb(255, 255, 255);
            "
          />
        </td>
      </table>
      <hr />
      <div>
        <img
          src="../../../assets/picture/任务.png"
          alt="任务名称"
          style="float: left; height: 50px; width: 50px; margin-left: 1%"
        />
        <div style="float: left; margin-left: 8%">
          任务介绍：求帮取快递，紫菘13栋快递点，5r
        </div>
        <div style="float: right; margin-right: 3%">
          <input type="button" value="详情" />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style scoped>
table {
  font-size: 28px;
  text-align: center;
  margin: 0px auto;
  width: 80%;
  height: 54px;
}
</style>