How to Develop and Contribute to rpcalc
=======================================

This project uses the [successful git branching model](http://nvie.com/posts/a-successful-git-branching-model/) and sticks closely to [semantic versioning](http://semver.org/).

## Releasing

After a release or hotfix branch is prepared, the following tasks will properly release the next version.

- Get rid of the `## _NEXT RELEASE_` section in `changelog.md`.
- Commit changes to master _e.g._ `git merge --no-ff hotfix-0.3.1`.
- Tag the release on master. Use an annotated tag with the name `v` followed by the semantic version number _e.g._ `git tag -a v0.3.1 -m 'squashes trig bugs'`.
- Commit changes to develop _e.g._ `git merge --no-ff hotfix-0.3.1`.
- `git checkout develop` and add a `## _NEXT RELEASE_` section in `changelog.md` before the latest version
- Go to the [page generator](https://github.com/qguv/rpcalc/generated_pages/new), hit _Load README.md_. Hit _Continue to Layouts_, choose the _Leap Day_ theme, and hit _Publish_.
