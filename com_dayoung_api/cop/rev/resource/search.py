# class ReviewSearch(Resource):
    
#     def get(self, movie_title):
#         print("SEARCH 진입")
#         print(f'제목 : {movie_title}')
#         review = ReviewDao.find_by_movie_title(movie_title)
#         # review = {review[i]: review[i + 1] for i in range(0, len(review), 2)}
#         # review = json.dump(review)
#         reviewlist = []
#         # for review in reviews:
#             # reviewdic
#         for rev in review:
#             reviewlist.append(rev.json())
#         # print(f’Review type : {type(review[0])}‘)
#         print(f'Review List: {reviewlist}')
#         return reviewlist[:]