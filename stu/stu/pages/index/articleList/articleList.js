const request = require('../../../utils/request.js');

Page({
  data: {
    words: [],
    currentPage: 1,
    isLoading: false,
    noMoreData: false,
    level: ''
  },

  onLoad(options) {
    console.log('onLoad options:', options);
    const level = options.level || '';
    this.setData({ level });
    this.fetchWordsByLevel(level, 1);
  },

  fetchWordsByLevel(level, page) {
    if (this.data.isLoading || this.data.noMoreData) return;

    this.setData({ isLoading: true });

    const param = {
      level: level,
      currentPage: page
    };

    request.post("/findArticlesList", param)
      .then(res => {
        console.log(res)
        const newWords = res.data.data || [];
        const isLastPage = newWords.length === 0;

        this.setData({
          words: page === 1 ? newWords : [...this.data.words, ...newWords],
          currentPage: page,
          isLoading: false,
          noMoreData: isLastPage
        });
      })
      .catch(() => {
        this.setData({ isLoading: false });
      });
  },

  onPullDownRefresh() {
    this.setData({
      currentPage: 1,
      noMoreData: false
    });
    this.fetchWordsByLevel(this.data.level, 1);
    wx.stopPullDownRefresh();
  },

  onReachBottom() {
    if (!this.data.noMoreData) {
      this.fetchWordsByLevel(this.data.level, this.data.currentPage + 1);
    } else {
      console.log('已加载完全部文章');
    }
  },

  navigateToWordDetail(event) {
    const wordId = event.currentTarget.dataset.id;
    wx.navigateTo({
      url: `/pages/index/articleData/articleData?id=${wordId}`
    });
  },

  onReady() {},
  onShow() {},
  onHide() {},
  onUnload() {},
  onShareAppMessage() {}
});
