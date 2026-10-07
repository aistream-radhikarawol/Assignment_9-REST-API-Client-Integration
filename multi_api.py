def main():
    
    print("====================================")
    print("       Multi-API Integration")
    print("====================================")

    username = input("Enter GitHub username: ")

    github_user = get_github_user(username)

    if github_user is None:
        return

    print("\nGitHub User:")
    print("Username:", github_user["login"])
    print("Name:", github_user["name"])
    print("Profile:", github_user["html_url"])

    user_id = 1

    posts = get_user_posts(user_id)

    print("\nPosts received:", len(posts))

    combined_data = combine_data(
        github_user,
        posts
    )

    save_json(combined_data)

    save_csv(combined_data)

    print("\nData integration completed successfully.")


if __name__ == "__main__":
    main()