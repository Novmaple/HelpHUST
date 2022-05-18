<template>
  <div class="sell">
    <div id="head1">
      <div style="margin-top: 5%; text-indent: 20em">商品图片:</div>
      <div style="text-align: center; margin-top: -3%; height: 20%">
        <el-upload
          class="avatar-uploader"
          action="https://jsonplaceholder.typicode.com/posts/"
          :show-file-list="false"
          :on-success="handleAvatarSuccess"
          :before-upload="beforeAvatarUpload"
        >
          <img v-if="imageUrl" :src="imageUrl" class="avatar" />
          <i v-else class="el-icon-plus avatar-uploader-icon"></i>
        </el-upload>
      </div>
    </div>
    <div id="head2">
      <div style="margin-top: 1%; text-indent: 20em">预设报价:</div>
      <div style="text-align: center; margin-top: -1.5%">
        <form>
          <input type="text" name="picture" />
        </form>
      </div>
    </div>
    <div id="head3">
      <div style="margin-top: 1%; text-indent: 20em">商品详细说明：</div>
      <div style="text-align: center; margin-top: -1.5%">
        <form>
          <input type="text" name="picture" />
        </form>
      </div>
    </div>
    <div id="head4">
      <div style="margin-top: 1%; text-indent: 20em">交付方式：</div>
      <div style="text-align: center; margin-top: -1.5%">
        <form>
          <input type="text" name="picture" />
        </form>
      </div>
    </div>
    <div id="head5">
      <div style="margin-top: 1%; text-indent: 20em">联系方式：</div>
      <div style="text-align: center; margin-top: -1.5%">
        <form>
          <input type="text" name="picture" />
        </form>
      </div>
    </div>
    <div style="text-align: center; margin-top: 2%">
      <form>
        <input
          type="submit"
          value="上传"
          style="
            height: 40px;
            width: 100px;
            background-color: rgb(11, 163, 233);
          "
        />
      </form>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      imageUrl: "",
    };
  },
  methods: {
    handleAvatarSuccess(res, file) {
      this.imageUrl = URL.createObjectURL(file.raw);
    },
    beforeAvatarUpload(file) {
      const isJPG = file.type === "image/jpeg";
      const isLt2M = file.size / 1024 / 1024 < 2;

      if (!isJPG) {
        this.$message.error("上传图片只能是 JPG 格式!");
      }
      if (!isLt2M) {
        this.$message.error("上传图片大小不能超过 2MB!");
      }
      return isJPG && isLt2M;
    },
  },
};
</script>
<style scoped>
#head0 {
  background-color: rgb(240, 230, 230);
  color: rgb(37, 4, 4);
  border: 1px solid rgb(26, 6, 6);
  height: 80px;
}
#head1 {
  color: black;
  height: 80px;
}
#head2 {
  color: black;
  height: 50px;
  border: 1px solid rgb(11, 163, 233);
}
#head3 {
  color: black;
  height: 50px;
  border: 1px solid rgb(26, 6, 6);
}
#head4 {
  color: black;
  height: 50px;
  border: 1px solid rgb(26, 6, 6);
}
#head5 {
  color: black;
  height: 50px;
  border: 1px solid rgb(26, 6, 6);
}
#head8 {
  background-color: rgb(43, 3, 3);
  color: white;
  border: 1px solid rgb(26, 6, 6);
  text-align: center;
  margin-top: 2%;
  height: 50px;
}
.avatar-uploader .el-upload {
  border: 1px dashed #d9d9d9;
  border-radius: 6px;
  cursor: pointer;
  position: relative;
  overflow: hidden;
}
.avatar-uploader .el-upload:hover {
  border-color: #409eff;
}
.avatar-uploader-icon {
  font-size: 28px;
  color: #8c939d;
  width: 178px;
  height: 178px;
  line-height: 60px;
  text-align: center;
}
.avatar {
  width: 178px;
  height: 178px;
  display: block;
}
</style>