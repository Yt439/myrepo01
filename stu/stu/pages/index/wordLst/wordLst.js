const request = require('../../../utils/request.js');

Page({
  data: {
    words: [],
    currentPage: 1,
    level: '',
    isLoading: false,
    noMoreData: false
  },

  onLoad(options) {
    const level = options.level;
    this.setData({ level });
    this.fetchWordsByLevel(level, 1);
  },

  fetchWordsByLevel(level, page) {
    if (this.data.isLoading || this.data.noMoreData) return;

    this.setData({ isLoading: true });

    const param = {
      type: level,
      currentPage: page
    };

    request.post("/findThesaurusList", param)
      .then(res => {
        const newWords = res.data.data || [];
        this.setData({
          words: page === 1 ? newWords : [...this.data.words, ...newWords],
          currentPage: page,
          isLoading: false,
          noMoreData: newWords.length === 0 // ★ 空数组说明没有更多
        });
      })
      .catch(() => {
        this.setData({ isLoading: false });
      });
  },

  onPullDownRefresh() {
    const { level } = this.data;
    this.setData({
      currentPage: 1,
      noMoreData: false
    });
    this.fetchWordsByLevel(level, 1);
    wx.stopPullDownRefresh();
  },

  onReachBottom() {
    if (!this.data.noMoreData) {
      this.fetchWordsByLevel(this.data.level, this.data.currentPage + 1);
    } else {
      console.log('已经加载完全部数据');
    }
  },

  navigateToWordDetail(event) {
    const wordId = event.currentTarget.dataset.id;
    wx.navigateTo({
      url: `/pages/index/wordData/wordData?id=${wordId}`
    });
  },

  onReady() {},
  onShow() {},
  onHide() {},
  onUnload() {},
  onShareAppMessage() {}
});
