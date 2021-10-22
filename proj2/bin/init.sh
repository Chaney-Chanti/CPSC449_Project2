sqlite-utils insert ./var/users.db users --csv ./share/users.csv --detect-types --pk=userId
sqlite-utils insert ./var/post.db post --csv ./share/post.csv --detect-types --pk=postId
sqlite-utils insert ./var/following.db following --csv ./share/following.csv --detect-types
sqlite-utils create-index ./var/users.db username passW email bio --unique
sqlite-utils add-foreign-key post.db post userID users userID 
sqlite-utils add-foreign-key post.db post orgPostID posts postID
sqlite-utils create-index ./var/posts.db userID orgPostID link content timestamp  --unique
sqlite-utils add-foreign-key following.db following influencerID users userID 
sqlite-utils add-foreign-key following.db following followerID users userID 
sqlite-utils create-index ./var/following.db influencerID  followerID --unique