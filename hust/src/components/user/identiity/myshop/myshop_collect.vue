<template>
  <div class="collect">
    <div id="head0">
      <h1>我的收藏</h1>
    </div>
    <div id="head2">
      <table border="2">
        <td>
          <form>
            <input
              type="button"
              value="创建收藏夹"
              style="height: 40px; width: 100px"
            />
          </form>
        </td>
        <td>
          <form>
            <input
              type="button"
              value="默认收藏夹"
              style="height: 40px; width: 100px"
            />
          </form>
        </td>
      </table>
    </div>

    <table border="big">
      <tr class="one">
        <th width="13%" height="80px" style="font-size: 150%">上架时间</th>
        <th width="13%" style="font-size: 150%">商品名称</th>
        <th width="13%" style="font-size: 150%">所属店铺</th>
        <th width="20%" style="font-size: 150%">商品描述</th>
        <th width="20%" style="font-size: 150%">商品价格</th>
        <th width="34%" style="font-size: 150%">评论区</th>
      </tr>

      <tr>
        <td height="80px">2021-03-12</td>
        <td>出二手卡西欧计算器</td>
        <td>沁苑山大王</td>
        <td>基本全新，用了不到一年</td>
        <td>原价140r 优惠60r 二手价80r</td>
        <td>
          <img
            src="https://img1.baidu.com/it/u=126957309,1078777871&fm=26&fmt=auto"
            style="width: 10%; height: 10%"
            alt="打开失败"
          />
          小刀一下，请问楼主60出吗
        </td>
      </tr>
      <tr>
        <td height="80px">2021-09-18</td>
        <td>二手小风扇</td>
        <td>西十二自习人</td>
        <td>大四学长用了一个夏天，便宜出了，便宜出了</td>
        <td>原价20r 优惠17r 二手价3r</td>
        <td>哇！好棒，请问小风扇出了吗？</td>
      </tr>
      <tr>
        <td height="80px">……</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td height="40px">……</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
      </tr>
    </table>
    <div id="head1">
      <p style="text-align: center">Hust.帮</p>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style scoped>
#head0 {
  background-color: rgb(240, 230, 230);
  color: rgb(37, 4, 4);
  border: 1px solid rgb(26, 6, 6);
  height: 80px;
}
#head1 {
  background-color: rgb(43, 3, 3);
  color: white;
  border: 1px solid rgb(26, 6, 6);
  text-align: center;
  margin-top: 1%;
  height: 50px;
}
#head2 {
  height: 80px;
  text-align: center;
}
.caption {
  text-align: center;
  font-family: "宋体";
  font-size: 200%;
  font-weight: 1000;
  letter-spacing: 20px;
}
#time {
  font-weight: 300px;
}
.slow {
  text-align: right;
  color: blue;
}
#slowy {
  text-align: right;
  color: blue;
}
table {
  font-size: 16px;
  text-align: center;
  margin: 3px auto;
  width: 60%;
}
</style>