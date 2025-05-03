const request = require('../../../utils/request.js');

Page({
  data: {
    username: '',
    email: '',
    address: '',
    password: '',
    confirmPassword: '',
  },

  // 获取用户数据
  onShow(options) {
    this.findUser();
  },

  findUser() {
    const userInfo = wx.getStorageSync('userInfo');
    const param = { user_id: userInfo.id };
    request.post("/FindUserView", param)
      .then(res => {
        console.log(res.data);
        this.setData({
          username: res.data.username || '',
          email: res.data.email || '',
          password: res.data.password || '',
          address: res.data.address || '',
        });
      })
      .catch(err => {
        console.error(err);
      });
  },

  // 处理表单提交
  onSubmit() {
    const { username, email, address, password, confirmPassword } = this.data;
    console.log("用户信息:", this.data);
    // 表单验证
    if (!username || !email || !address || !password || !confirmPassword) {
      wx.showToast({
        title: '请填写所有字段',
        icon: 'none',
      });
      return;
    }

    if (password !== confirmPassword) {
      wx.showToast({
        title: '密码不一致',
        icon: 'none',
      });
      return;
    }
    const userInfo = wx.getStorageSync('userInfo');
    // 提交数据
    request.post("/UpdateUserView", {
      username,
      email,
      address,
      password,
      user_id:userInfo.id
    })
      .then(response => {
        wx.showToast({
          title: '保存成功',
          icon: 'success',
          duration: 1000,  // 等待1秒后跳转，保证toast能显示
        });
      
        // 延迟跳转，避免toast没来得及显示
        setTimeout(() => {
          wx.switchTab({
            url: '/pages/user/user',
          });
        }, 1000);
        
      })
      .catch(err => {
        console.error(err);
        wx.showToast({
          title: '保存失败',
          icon: 'none',
        });
      });
  },

  // 更新用户名
  onUsernameInput(e) {
    console.log('输入的用户名:', e.detail);  // 查看输入的用户名
    this.setData({
      username: e.detail,
    });
  },

  // 更新邮箱
  onEmailInput(e) {
    console.log('输入的邮箱:', e.detail);  // 查看输入的邮箱
    this.setData({
      email: e.detail,
    });
  },

  // 更新地址
  onAddressInput(e) {
    console.log('输入的地址:', e.detail);  // 查看输入的地址
    this.setData({
      address: e.detail,
    });
  },

  // 更新密码
  onPasswordInput(e) {
    console.log('输入的密码:', e.detail);  // 查看输入的密码
    this.setData({
      password: e.detail,
    });
  },

  // 更新确认密码
  onConfirmPasswordInput(e) {
    console.log('输入的确认密码:', e.detail);  // 查看输入的确认密码
    this.setData({
      confirmPassword: e.detail,
    });
  },
});
