// pages/user-profile/user-profile.js
const request = require('../../utils/request.js');
Page({
  data: {
    userInfo: {},
    records: [
      { id: 1, date: '2025-02-01', score: 85 },
      { id: 2, date: '2025-02-03', score: 90 },
      { id: 3, date: '2025-02-05', score: 78 },
    ],
  },

  onShow(options) {
    this.findUser();
  },

  findUser(){
    const userInfo = wx.getStorageSync('userInfo');
    param = {
      user_id:userInfo.id
    }
    request.post("/FindUserView", param)
      .then(res => {
        console.log(res.data)
        this.setData({
          userInfo: {
            ...res.data,
            img: 'http://localhost:8000' + res.data.img  // 拼接成完整地址
          }
        })
        console.log(this.data.userInfo)
      })
      .catch(err => {
      });
  },

  onImgError(e) {
    console.error('图片加载失败：', e.detail.errMsg);
  },
  

  // 修改头像
  changeAvatar() {
    wx.chooseImage({
      count: 1,
      sizeType: ['original', 'compressed'],
      sourceType: ['album', 'camera'],
      success: (res) => {
        const userInfo = wx.getStorageSync('userInfo');
        const tempFilePath = res.tempFilePaths[0];
        
        // 上传图片
        wx.uploadFile({
          url: 'http://localhost:8000/upload_avatar',  // Django 接口地址
          filePath: tempFilePath,
          name: 'avatar',  // 这里是表单中的字段名
          formData: {
            user_id: userInfo.id,  // 传递用户ID，服务器用来找到对应的用户
          },
          header: {
            'Content-Type': 'multipart/form-data',  // 设置为文件上传格式
          },
          success: (uploadRes) => {
            const data = JSON.parse(uploadRes.data);
            if (data.success) {
              // 更新头像 URL
              this.findUser();
              wx.showToast({
                title: '头像修改成功',
                icon: 'success',
              });
            } else {
              wx.showToast({
                title: '头像上传失败',
                icon: 'none',
              });
            }
          },
          fail: () => {
            wx.showToast({
              title: '上传失败，请重试',
              icon: 'none',
            });
          }
        });
      },
    });
  },  

  // 跳转到答题记录页面
  goToRecords() {
    wx.navigateTo({
      url: '/pages/user/record/record',
    });
  },

  // 跳转到修改用户信息页面
  goToEditProfile() {
    wx.navigateTo({
      url: '/pages/user/updateuser/updateuser?userInfo=' + JSON.stringify(this.data.userInfo),
    });
  },

  logout() {
    wx.showModal({
      title: '提示',
      content: '确定要退出登录吗？',
      success: (res) => {
        if (res.confirm) {
          // 清除本地存储的用户信息
          wx.removeStorageSync('userInfo');
          this.setData({
            userInfo: {
              img: '',
              username: '未登录'
            }
          });
          wx.showToast({
            title: '已退出登录',
            icon: 'success',
            duration: 1000,
            success: () => {
              // 延迟一会再跳转，确保 toast 显示完
              setTimeout(() => {
                wx.reLaunch({
                  url: '/pages/login/login' // 请根据实际路径修改
                });
              }, 1000);
            }
          });
        }
      }
    });
  }
  


});