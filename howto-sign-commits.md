# How to sign a commit to Hiero

## Prepare email address

For this task you need an email address verified by GitHub.
It's configured in your GitHub Account, connected
to your GPG key and used in your git client.
If you marked the Checkbox "Keep my email addresses private"
in "Settings" -> "Emails" in your GitHub Account,
use the `noreply` email given by GitHub. 

* [GitHub Docs: Setting your commit email address](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-email-preferences/setting-your-commit-email-address)
* [GitHub Docs: Verifying your email address](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-email-preferences/verifying-your-email-address)

## Generate a new GPG key pair

To generate the required GPG key pair, you need the gpg command line tool
and the email address from the former step.

* [GitHub Docs: Generating a new GPG key](https://docs.github.com/en/authentication/managing-commit-signature-verification/generating-a-new-gpg-key)

## Associate your GPG key with your GitHub account

Add your GPG public key into your GitHub account.
With this step GitHub is ready to verify your PGP signed commits.

* [Adding a GPG key to your GitHub account](https://docs.github.com/en/authentication/managing-commit-signature-verification/adding-a-gpg-key-to-your-github-account)

## Work with your local git

Clone the repository you want to work on. Use git or the IDE of your choice.
Configure name and email needed (from the beginning) for this git repository.
Using the --global option configures them for all repositories.

```
git config set [--global] user.name "<your name>"
git config set [--global] user.email <your prepared email address from the beginning>
```

Now you can commit your changes on the command line.
You will be asked for the password of the private key.

```
# show the key id you need
gpg -k
# commit request
git commit -s -S<your key id> -m "<your comment>" .
# -s option: add a sign-off-by trailer by the committer
# -S<your key id> (no space after -S): GPG-sign commit
```

## Automate the required tasks in git

After applying the following two configuration steps,
the additional commit parameters aren't needed any more.
```
# commit request without additional parameters:
git commit -m "<your comment>" .
```

### GPG signing

```
# sign commits in this local repository by default
git config set commit.gpgsign true
# use this GPG key by default
git config set user.signingkey <your key id>
```

### DCO signature

> [!CAUTION]
> The following parameter is restricted to patch generation and not effective here.
> 
> git config set format.signOff true

No configuration parameter exists in git for this task.
The solution is using a hook, a script that is
automatically executed during each commit.
The script fortunately is already part of git.
It's located in the repository in the directory `.git/hooks/`.
Copy the file `prepare-commit-msg.sample` to `prepare-commit-msg`.
Uncomment the following lines at the end.

```
 SOB=$(git var GIT_COMMITTER_IDENT | sed -n 's/^\(.*>\).*$/Signed-off-by: \1/p')
 git interpret-trailers --in-place --trailer "$SOB" "$COMMIT_MSG_FILE"
 if test -z "$COMMIT_SOURCE"
 then
   /usr/bin/perl -i.bak -pe 'print "\n" if !$first_line++' "$COMMIT_MSG_FILE"
 fi
```

## Use everything in IntelliJ IDEA

IntelliJ uses git you have already configured in the former step.
You don't need to do anything.

The GPG signing can be configured here:
```
"Settings" -> "Version Control" -> "git" -> "Configure GPG Key"
```

The DCO signature can not be configured in IntelliJ, you need to do this in git.
