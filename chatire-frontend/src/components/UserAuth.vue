<template>
  <div class="container">
    <h1>欢迎来到chatire</h1>
    <div id="auth-container" class="row">
      <div class="col-sm-4 offset-sm-4">
        <ul class="nav nav-tabs nav-justified" id="myTab" role="tablist">
          <li class="nav-item">
            <a class="nav-link active" id="signup-tab" data-toggle='tab' href="#signup" role="tab" aria-controls="signup" aria-selected="true">注册</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" id="signin-tab" data-toggle="tab" href="#signin" role="tab" aria-controls="signin" aria-selected="false">登录</a>
          </li>
        </ul>
        <div class="tab-content" id="myTabContent">
          <div class="tab-pane fade show active" id="signup" role="tabpanel" aria-labelledby="signin-tab">
            <form @submi.prevent="signUp">
              <div class="form-group">
                <input v-model="email" type="email" class="form-control" id="email" placeholder="邮箱地址" required>
              </div>
              <div class="form-row">
                <div class="form-group col-md-6">
                  <input v-model="username" type="text" class="form-control" id="username" placeholder="用户名" required>
                </div>
                <div class="form-group col-md-6">
                  <input v-model="password" type="password" class="form-control" id="password" placeholder="密码" required>
                </div>
              </div>
              <div class="form-group">
                <div class="form-check">
                  <input class="form-check-input" type="checkbox" id="toc" required>
                  <label class="form-check-label" for="gridCheck">接受注册协议</label>
                </div>
              </div>
              <button type="submit" class="btn btn-block btn-primary">注册</button>
            </form>
          </div>
          <div class="tab-panel fade" id="signin" role="tabpanel" aria-labelledby="signin-tab">
            <form @submit.prevent="signIn">
              <div class="form-group">
                <input v-model="username" type="text" class="form-control" id="username" placeholder="用户名" required>
              </div>
              <div class="form-group">
                <input v-model="password" type="password" class="form-control" id="password" placeholder="密码" required>
              </div>
              <button type="submit" class="btn btn-block btn-primary">登录</button>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
const $ = window.jQuery

export default {
  data() {
    return {
      email: '',
      username: '',
      password: ''
    }
  },

  methods: {
    signUp() {
      $.post('http://localhost:8000/auth/users/create/', this.$data, (data) => {
        alert('您的账号已创建，即将为你自动登录！')
        this.signIn()
      })
        .fail((response) => {
          alert(response.responseText)
        })
    },
    signIn() {
      const credentials = { username: this.username, password: this.password }
      $.post('http://localhost:8000/auth/jwt/create/', credentials, (data) => {
        sessionStorage.setItem('authToken', data.token)
        sessionStorage.setItem('username', this.username)
        this.$router.push('/chats')
      })
        .fail((response) => {
          alert(response.responseText)
        })
    }
  }
}
</script>

<style scoped>
  #auth-container {
    margin-top: 50px
  }

  .tab-content {
    padding-top: 20px
  }
</style>

