$(document).ready(function() {
    var progressBar = $(".progressbar")
    $(window).load(function() {
        progressBar.addClass("stopped");
    });
    $(document).ajaxStart(function() {
        app.$data.state.loading = true;
    }).ajaxComplete(function() {
        app.$data.state.loading = false;
    });

    document.getElementById("file").onchange = function() {
        f = document.getElementById("file").files[0];
        if(f === undefined) {
            app.$data.state.fileChosen = false;
        } else {
            app.$data.state.fileChosen = true;
            fr = new FileReader();
            fr.onload = function(e) {
                app.$data.postForm.data = e.target.result;
                app.$data.postForm.filename = f.name;
            };
            fr.readAsDataURL(f);
        }
    };

    // vue

    username = window.location.pathname.split("@").reverse()[0];
            
    function getData() {
        $.get("/@" + username + "/profile").done(function(data) {
            app.$data.profile = data;
        }).fail(function(xhr) {
            app.$data.state.notFound = true;
        });

        $.get("/@" + username + "/posts").done(function(data) {
            app.$data.posts = data;
        }).fail(function(xhr) {
            app.$data.state.notFound = true;
        });

        $.get("/session").done(function(data) {
            app.$data.session = data;
        });
    };

    app = new Vue({
        el: "#app",
        data: {
            profile: {
                username: "",
                name: "",
                description: "",
                followerCount: 0,
                followingCount: 0,
                isFollowing: undefined,
            },
            posts: [],
            session: {},
            signInForm: {
                username: "",
                password: "",
                error: false
            },
            signUpForm: {
                username: "",
                password: "",
                password2: "", 
                contact: {
                    email: ""
                }
            },
            postForm: {
                title: "",
                description: "",
                data: "",
                filename: ""
            },
            state: {
                notFound: false,
                unauthorized: false,
                edittingProfile: false,
                signingUp: false,
                signingIn: false,
                loading: true,
                fileChosen: false,
                tab: "profile"
            }
        },
        methods: {
            getData: getData, 
            login: function() {
                $.ajax("/session", {
                    data: JSON.stringify(app.$data.signInForm),
                    type: "post",
                    contentType: "application/json"
                }).done(function(data) {
                    app.$data.state.signingIn = false;
                    app.$data.session = data;
                }).fail(function(xhr) {
                    app.$data.signInForm.error = true;
                });
            },
            logout: function() {
                $.ajax("/session", {
                    "type": "delete"
                }).always(function(data) {
                    app.$data.session = {};
                });
            },
            updateProfile: function() {
                $.ajax("/@" + username + "/settings", {
                    data: JSON.stringify(app.$data.profile),
                    type: "post",
                    contentType: "application/json"
                }).fail(function(xhr) {
                    if(xhr.status === 404) {
                        app.$data.state.signingIn = true;
                    }
                })
                app.$data.state.edittingProfile = false;
                getData();
            },
            signUp: function() {
                /*$.ajax({
                    type: "post",
                    url: "/signup",
                    contentType: "application/json",
                    data: app.$data.signUpForm
                });*/
                $.ajax("/signup", {
                    data: JSON.stringify(app.$data.signUpForm),
                    type: "post",
                    contentType: "application/json"
                }).done(function(data) {
                    location.href = "/@" + app.$data.signUpForm.username;
                });
            },
            follow: function() {
                $.ajax("/@" + username + "/profile/followers", {
                    type: "post",
                    contentType: "application/json"
                }).done(function(data) {
                    getData();
                }).fail(function(xhr) {
                    if(xhr.status === 404) {
                        app.$data.state.notFound = true;
                    } else if(xhr.status === 401) {
                        app.$data.state.signingIn = true;
                    }
                });
                getData();
            },
            unfollow: function() {
                $.ajax("/@" + username + "/profile/followers", {
                    type: "delete",
                    contentType: "application/json"
                }).done(function(data) {
                    getData();
                }).fail(function(xhr) {
                    if(xhr.status === 404) {
                        app.$data.state.notFound = true;
                    } else if(xhr.status === 401) {
                        app.$data.state.signingIn = true;
                    }
                });
                getData();
            },
            uploadPost: function() {
                $.ajax("/@" + username + "/posts", {
                    type: "post",
                    data: JSON.stringify(app.$data.postForm),
                    contentType: "application/json"
                }).done(function(data) {
                    app.$data.state.fileChosen = false;
                    getData();
                }).fail(function(xhr) {
                    if(xhr.status === 401) {
                        app.$data.state.notFound = true;
                    } else if(xhr.status === 403) {
                        location.reload();
                    }
                });
            },
            cancelPost: function() {
                app.$data.state.fileChosen = false;
                app.$data.postForm.filename = "";
                app.$data.postForm.description = "";
            }
        }
    });
    $(document).ready(function() {
        app.getData();
    });

});