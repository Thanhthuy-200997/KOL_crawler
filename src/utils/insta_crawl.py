import instaloader
from instaloader import Instaloader, Profile, Post
from utils.user_login import *
from datetime import datetime


class InstaCrawler:
    def __init__(self) -> None:
        super(InstaCrawler, self).__init__()
        self.ic = Instaloader()
        if login:
            try:
                login()
            except Exception as e:
                print(e)
                raise Exception
    def get_profile(self, username: str) -> Profile:
        profile = Profile.from_username(self.ic.context, username)
        return profile
    
    def get_profile_meta(self, profile: Profile) -> dict[str, any]:
        profile_meta = {
            "id": str(profile.userid),
            "username": profile.username,
            "insta_url": f"https://www.instagram.com/{profile.username}/",
            "is_private": profile.is_private,
            "igtv": profile.igtvcount,
            "followers": profile.followers,
            "following": profile.followees,
            "external_url": profile.external_url,
            "is_business_account": profile.is_business_account,
            "business_category_name": profile.business_category_name,
            "biography": profile.biography,
            "full_name": profile.full_name,
            "is_verified": profile.is_verified,
            "profile_pic_url": profile.profile_pic_url
        }

        return profile_meta
    
    def get_post_meta(self, post: Post) -> dict[str, any]:
        if post.typename == 'GraphSidecar':
            tmp = [node.display_url for node in post.get_sidecar_nodes()]
        else:
            tmp = [post.url]

        post_meta = {
            "mediaid": str(post.mediaid),
            "uuid" : post.shortcode,
            "insta_url": f"https://instagram.com/p/{post.shortcode}/",
            "post_date_local": post.date_local,
            "links": tmp,
            "mtime": post.date_utc
        }

        return post_meta    


    # def get_posts(self, profile: Profile, user_meta: dict, max_limit: int = 12) -> list[Post]:
    #     count = 0
    #     posts = profile.get_posts()
    #     if 'posts' not in user_meta:
    #         user_meta['posts'] = []
    #     for idx, post in enumerate(posts):
    #         post_meta = self.get_post_meta(post)
    #         count += 1
    #         if count >= max_limit:
    #             break
            
    #         #lastest post date:
    #         if idx == 0:
    #             user_meta['lastest_upload'] = post_meta['post_date_local']
            
    #         user_meta['posts'].append(post_meta)

    #     return user_meta
    
    # def download_post(self,profile: Profile,path:str):
    #     uploaded_posts = profile.get_posts()
    #     insta = Instaloader(dirname_pattern = path)
    #     insta.download_pictures = True
    #     insta.download_comments = False
    #     insta.download_geotags = False
    #     insta.download_videos = False
    #     insta.save_metadata = False
    #     insta.download_video_thumbnails = False
    #     insta.post_metadata_txt_pattern = ''
    #     for post in uploaded_posts:
    #         print(post.date_utc)
    #         if post.date_utc >= datetime(2021, 1, 1, 0, 0, 0):
    #             insta.download_post(post,target=profile.username)
    #         else:
    #             pass
    #     return None
    
    def get_posts(self, profile: Profile, user_meta: dict) -> list[Post]:
        posts = profile.get_posts()
        if 'posts' not in user_meta:
            user_meta['posts'] = []
        for idx, post in enumerate(posts):
            if post.date_utc >= datetime(2022, 6, 1, 0, 0, 0):
                post_meta = self.get_post_meta(post)
                if idx == 0:
                    user_meta['lastest_upload'] = post_meta['post_date_local']
            
                user_meta['posts'].append(post_meta)

        return user_meta
    

 