import os,sys
import json

import facebook

if __name__ == '__main__':
    token = "EAANXc609TdkBAO3HmSoswBZCTIbmZBMOcdzvLa8c97fdDZBzCjZCL2vAhJYPhyKt5sURY5VlozyHOZABZB6lxrPU5Bb8jM0PLFHh0xCj376nqu6EQZA6PoGbnI1cKyGYiOtrNNyLUebm55GGjNGI5VL6Tj1R9IstsIUSQHBbW7WVP7ZBUbZAn4occ"
    

    graph = facebook.GraphAPI(access_token=token, version = 3.0)
    #profile = graph.get_object('974146599436745_974147879436617',fields='get_connections')
    likes = graph.get_object(id='974146599436745_974530109398394', fields='shares,likes.summary(true),comments.summary(true)')

    ##GENERAL INFO##
    about = graph.get_object(id='974146599436745', fields='about')
    country_page_likes = graph.get_object(id='974146599436745', fields='country_page_likes')
    fan_count = graph.get_object(id='974146599436745', fields='fan_count')
    location = graph.get_object(id='974146599436745', fields='location')
    new_like_count = graph.get_object(id='974146599436745', fields='new_like_count')
    page_token =  graph.get_object(id='974146599436745', fields='page_token')
    notifications = graph.get_object(id='974146599436745', fields='notifications')
    posts = graph.get_object(id='974146599436745', fields='posts')



    ##PAGE INSIGHTS
    page_content_activity_by_action_type_unique = graph.get_object(id='974146599436745', fields='insights.metric(page_content_activity_by_action_type_unique).period(week)')
    page_content_activity_by_age_gender_unique = graph.get_object(id='974146599436745', fields='insights.metric(page_content_activity_by_age_gender_unique).period(week)')
    page_content_activity_by_country_unique = graph.get_object(id='974146599436745', fields='insights.metric(page_content_activity_by_country_unique).period(week)')
    page_content_activity_by_locale_unique = graph.get_object(id='974146599436745', fields='insights.metric(page_content_activity_by_locale_unique).period(week)')
    page_content_activity = graph.get_object(id='974146599436745', fields='insights.metric(page_content_activity).period(week)')
    
    post_activity_unique =  graph.get_object(id='974146599436745_974147879436617', fields='insights.metric(post_activity_unique)')

    page_impressions = graph.get_object(id='974146599436745', fields='insights.metric(page_impressions).period(day)')
    page_impressions_unique = graph.get_object(id='974146599436745', fields='insights.metric(page_impressions_unique).period(week)')
    page_impressions_by_story_type =graph.get_object(id='974146599436745', fields='insights.metric(page_impressions_by_story_type).period(day)')
    page_impressions_frequency_distribution = graph.get_object(id='974146599436745', fields='insights.metric(page_impressions_frequency_distribution).period(week)')
    page_impressions_by_age_gender_unique=graph.get_object(id='974146599436745', fields='insights.metric(page_impressions_by_age_gender_unique).period(week)')

    page_engaged_users = graph.get_object(id='974146599436745', fields='insights.metric(page_engaged_users).period(week)')
    page_post_engagements = graph.get_object(id='974146599436745', fields='insights.metric(page_post_engagements).period(week)')
    page_consumptions =  graph.get_object(id='974146599436745', fields='insights.metric(page_post_engagements).period(week)')
    page_consumptions_unique = graph.get_object(id='974146599436745', fields='insights.metric(page_consumptions_unique).period(week)')
    
    ##
    page_negative_feedback = graph.get_object(id='974146599436745', fields='insights.metric(page_negative_feedback).period(week)')
    page_positive_feedback_by_type=graph.get_object(id='974146599436745', fields='insights.metric(page_positive_feedback_by_type).period(week)')
    page_fans_online = graph.get_object(id='974146599436745', fields='insights.metric(page_fans_online)')
    page_fans_online_per_day = graph.get_object(id='974146599436745', fields='insights.metric(page_fans_online_per_day)')
    page_fan_adds_by_paid_non_paid_unique = graph.get_object(id='974146599436745', fields='insights.metric(page_fan_adds_by_paid_non_paid_unique)')
    
    page_actions_post_reactions_like_total = graph.get_object(id='974146599436745', fields='insights.metric(page_actions_post_reactions_like_total)')
    page_total_actions = graph.get_object(id='974146599436745', fields='insights.metric(page_total_actions)')
    
    ##DEMOGRAPHICS
    page_fans_locale = graph.get_object(id='974146599436745', fields='insights.metric(page_fans_locale)')
    page_fans_city = graph.get_object(id='974146599436745', fields='insights.metric(page_fans_city)')
    page_fans_country = graph.get_object(id='974146599436745', fields='insights.metric(page_fans_country)')
    page_fans_gender_age = graph.get_object(id='974146599436745', fields='insights.metric(page_fans_gender_age)')
    page_fan_adds = graph.get_object(id='974146599436745', fields='insights.metric(page_fan_adds)')
    page_fan_removes = graph.get_object(id='974146599436745', fields='insights.metric(page_fan_removes)')
    page_fans_by_unlike_source_unique = graph.get_object(id='974146599436745', fields='insights.metric(page_fans_by_unlike_source_unique)')
   
   
    ##
    page_tab_views_login_top_unique = graph.get_object(id='974146599436745', fields='insights.metric(page_tab_views_login_top_unique)')
    page_views_total = graph.get_object(id='974146599436745', fields='insights.metric(page_views_total)')
    page_views_external_referrals = graph.get_object(id='974146599436745', fields='insights.metric(page_views_external_referrals)')
    page_views_by_profile_tab_logged_in_unique = graph.get_object(id='974146599436745', fields='insights.metric(page_views_by_profile_tab_logged_in_unique)')
    page_views_by_internal_referer_logged_in_unique = graph.get_object(id='974146599436745', fields='insights.metric(page_views_by_internal_referer_logged_in_unique)')
    #page_views_by_referers_logged_in_unique = graph.get_object(id='974146599436745', fields='insights.metric(page_views_by_referers_logged_in_unique)')
    
    ##PAGE POST
    page_posts_impressions = graph.get_object(id='974146599436745', fields='insights.metric(page_posts_impressions).period(week)')
    page_posts_impressions_unique = graph.get_object(id='974146599436745', fields='insights.metric(page_posts_impressions_unique)')
    page_posts_impressions_frequency_distribution = graph.get_object(id='974146599436745', fields='insights.metric(page_posts_impressions_frequency_distribution)')
    
    ##POSTS
    post_impressions = graph.get_object(id='974146599436745_974147879436617', fields='insights.metric(post_impressions)')
    post_impressions_fan = graph.get_object(id='974146599436745_974147879436617', fields='insights.metric(post_impressions_fan)')
    post_reactions_by_type_total = graph.get_object(id='974146599436745_974147879436617', fields='insights.metric(post_reactions_by_type_total)')
    
    page_content_activity_by_city_unique =graph.get_object(id='974146599436745', fields='insights.metric(page_content_activity_by_city_unique)')

    page_impressions_by_country_unique = graph.get_object(id='974146599436745', fields='insights.metric(page_impressions_by_country_unique)')
    page_impressions_by_city_unique = graph.get_object(id='974146599436745', fields='insights.metric(page_impressions_by_city_unique)')
    page_fans_by_like_source = graph.get_object(id='974146599436745', fields='insights.metric(page_fans_by_like_source)')
    
    page_content_activity_by_city_unique = graph.get_object(id='974146599436745', fields='insights.metric(page_content_activity_by_city_unique)')
    page_impressions_by_city_unique = graph.get_object(id='974146599436745', fields='insights.metric(page_impressions_by_city_unique)')
    page_fans_city= graph.get_object(id='974146599436745', fields='insights.metric(page_fans_city)')
    
    page_fans = graph.get_object(id='974146599436745', fields='insights.metric(page_fans)')

    page_content_activity_by_action_type = graph.get_object(id='974146599436745', fields='insights.metric(page_content_activity_by_action_type)')
    page_impressions_by_country_unique = graph.get_object(id='974146599436745', fields='insights.metric(page_impressions_by_country_unique).date_preset(last_7d)')
    #ad_campaign = graph.get_object(id='974146599436745', fields='ad_campaign')
    page_content_activity_by_country_unique = graph.get_object(id='974146599436745', fields='insights.metric(page_content_activity_by_country_unique).date_preset(last_7d)')
    page_content_activity_by_city_unique = graph.get_object(id='974146599436745', fields='insights.metric(page_content_activity_by_city_unique).date_preset(last_7d)')
    
    #content_temp_end_time=page_content_activity_by_city_unique["insights"]["data"][0]['values'][0]['end_time']
    #content_temp_value=page_content_activity_by_city_unique["insights"]["data"][0]['values'][0]['value']
    
    page_impressions_by_locale_unique = graph.get_object(id='974146599436745', fields='insights.metric(page_impressions_by_locale_unique).date_preset(last_7d)')
    page_content_activity_by_locale_unique = graph.get_object(id='974146599436745', fields='insights.metric(page_content_activity_by_locale_unique).date_preset(last_7d)')
    

    ##latest
    page_posts_impressions_viral = graph.get_object(id='974146599436745', fields='insights.metric(page_posts_impressions_viral).period(week)')
    post_clicks = graph.get_object(id='974146599436745_974147879436617', fields='insights.metric(post_clicks)')
    post_reactions_by_type_total = graph.get_object(id='974146599436745_974147879436617', fields='insights.metric(post_reactions_by_type_total)')
    page_fans_by_like_source = graph.get_object(id='974146599436745', fields='insights.metric(page_fans_by_like_source)')
    page_positive_feedback_by_type = graph.get_object(id='974146599436745', fields='insights.metric(page_positive_feedback_by_type)')
    page_consumptions = graph.get_object(id='974146599436745', fields='insights.metric(page_consumptions).period(week)')

     
    page_actions_post_reactions_total= graph.get_object(id='974146599436745', fields='insights.metric(page_actions_post_reactions_total)')
    page_fan_adds_by_paid_non_paid_unique = graph.get_object(id='974146599436745', fields='insights.metric(page_fan_adds_by_paid_non_paid_unique)')
    post_reactions_by_type_total = graph.get_object(id='974146599436745_974147879436617', fields='insights.metric(post_reactions_by_type_total)')
    print (json.dumps(page_fans_city, indent=4))