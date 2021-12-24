every thing is nullable expect somethings which is must
every date will be timestamp until something change

-django users
    email
    password

_profiles
    -fields
        field[backend-ui-designer]

    -country
        name

    -city
        name

    -phone_number
        profile_id
        name
        number

    -contact_info [fb,email,github,etc] 
        profile_id
        name
        url
        #icons fl dashboard

    -profile
        user
        fields_id
        name
        country_id
        city_id
        about
        job_title
        image
        birthday



_work_experience
    -organizations
        name
        icon

    -work_experience
        profile_id
        organization_id
        start_date          
        end_date 

    -work_experience_bullet_points
        work_experience_id
        point_text



_education
    -education
        profile_id
        organization_id
        start_date          
        end_date       

    -courses
        education_id
        name
        start_date
        end_date
        course_expected_time
        certificate_file
        certificate_url
        highlight



_projects
    -projects
        profile_id
        name
        description
        start_date
        end_date
        preview
        icon
        icon_url

    -project_bullet_points
        project_id
        point_text

    -project_urls
        project_id
        name
        url




_skills
    -categories
        name
    -skills
        name
        category_id
    -user_skills
        profile_id
        skill_id
        projects_number
        sample_url




_achievement
    -achievement
        profile_id
        text
    -hyperlinks
        achievement_id
        url
        start_index
        end_index