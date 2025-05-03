// pages/index/wordLevel/wordLevel.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    wordLevels: ['beginner', 'intermediate', 'advanced'],
  },
  navigateToLevel(event) {
    const level = event.currentTarget.dataset.level;
    // console.log("点击了等级：" + level)
    wx.navigateTo({
      url: `/pages/index/wordLst/wordLst?level=${level}`,
    });
  },

})