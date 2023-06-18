# KOL_crawler
This is crawl data from instagram and tiktok with list KOL/influencer

## Instagram:
Using Instaloader.

Input (in data): file txt include KOL/influencer which you have

Output (in result): file json with information metapost and their image post from 6/2022 to now.

With each account: use method get_profile to return profile meta. Then, use method get_post to return metapost (using get_posts is the 
first function to set limit post). Finally, with links in meta post send request to download image.

To run: py main.py

Let see: https://instaloader.github.io/

![image](https://github.com/Thanhthuy-200997/KOL_crawler/assets/92812173/f1aa668c-f880-470b-844a-88d99db0004c)


## TikTok
