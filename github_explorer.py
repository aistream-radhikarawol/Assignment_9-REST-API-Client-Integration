def main():
    
    print("====================================")
    print("       GitHub API Explorer")
    print("====================================")

    keyword = input("Enter repository search keyword: ")

    repositories = search_repositories(
        keyword,
        page=1,
        per_page=10
    )

    display_repositories(repositories)

    save_to_csv(repositories)

    if repositories:

        print("\nEnter repository details.")
        owner = input("Enter owner name: ")
        repo = input("Enter repository name: ")

        details = get_repository_details(owner, repo)
        display_repository_details(details)

        commits = get_commits(owner, repo)
        display_commits(commits)

        issues = get_issues(owner, repo)
        display_issues(issues)


if __name__ == "__main__":
    main()