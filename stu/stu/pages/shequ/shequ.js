const request = require('../../utils/request.js');
Page({

  /**
   * 页面的初始数据
   */
  data: {
    announcements: [],  // 存储公告列表
    finished: false,    // 控制是否已经加载完所有数据
    page: 1,            // 当前页数
    perPage: 10,        // 每页加载的公告数量
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad(options) {
    this.loadMoreAnnouncements();
  },

  loadMoreAnnouncements() {
    const { page, perPage, announcements } = this.data;

    const newAnnouncements = this.fetchAnnouncements(page, perPage);
    console.log('New Announcements:', newAnnouncements);  // 打印新加载的公告数据

  },

  // 模拟获取公告数据
  fetchAnnouncements(page, perPage) {
    const param = {
    }
    request.post("/findAnnouncementList",param)
    .then(res=>{
      this.setData({
        words: res.data.data,
      });
      this.setData({
        announcements: res.data.data,
        // page: page + 1,
        // finished: newAnnouncements.length < perPage, // 判断是否还有更多数据
      });
    }).catch(res=>{
    })
    
  },

  // 点击进入公告详情页
  goToAnnouncementDetail(event) {
    const announcementId = event.currentTarget.dataset.id;
    wx.navigateTo({
      url: `/pages/shequ/tongzhi/tongzhi?id=${announcementId}`, // 跳转到公告详情页
    });
  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady() {
  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow() {
  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide() {
  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload() {
  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh() {
  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom() {
    this.loadMoreAnnouncements();  // 上拉加载更多
  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage() {
  }
})
