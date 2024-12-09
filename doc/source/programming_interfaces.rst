Description of the programming interfaces
=========================================

This section provides a detailed overview of the programming interfaces in the OC_Lettings_Site project.
It includes descriptions of views, models, and test cases, organized by application. 

- OC_Lettings_Site
    - tests
        - test_urls
            - test_index_url()
            - test_lettings_url()
            - test_profiles_url()
        - test_views
            - test_index_view()
            - test_index_view_template()
    - views
        - index()
        - handler_404()
        - handler_500()

- lettings
    - tests
        - test_models
            - test_address_creation()
            - test_invalid_number()
            - test_invalid_state_lenght()
            - test_invalid_country_code()
            - test_letting_creation()
            - test_letting_invalid_title()
        - test_urls
            - test_index_url()
            - test_non_existent_url()
        - test_views
            - test_index_view()
            - test_letting_view()
            - test_letting_detail_integration()
    - models
        - Address
            - Address.number
            - Address.street
            - Address.city
            - Address.state
            - Address.zip_code
            - Address.country_iso_code
        - Letting
            - Letting.title
            - Letting.address
    - views
        - index()
        - letting()

- profiles
    - tests
        - test_models
            - test_profile_creation()
            - test_profile_city()

        - test_urls
            - test_index_url()
            - test_profile_url()

        - test_views
            - test_index_view()
            - test_index_view_no_profiles()
            - test_profile_view()
            - test_profile_detail_integration()
    - models
        - Profile.user
        - Profile.favorite_city
    - views
        - index()
        - profile()
