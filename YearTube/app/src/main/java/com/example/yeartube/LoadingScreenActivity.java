package com.example.yeartube;

import android.annotation.SuppressLint;
import android.content.Intent;
import android.os.AsyncTask;
import android.os.Bundle;
import android.os.Handler;
import android.util.Log;
import android.widget.ProgressBar;
import android.widget.TextView;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.ProtocolException;
import java.net.URL;
import java.net.URLEncoder;

import okhttp3.MediaType;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.RequestBody;
import okhttp3.Response;

public class LoadingScreenActivity extends AppCompatActivity {

    private TextView textView;
    private ProgressBar progressBar;
    String str;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_loading_screen);

        textView = findViewById(R.id.loading_text);
        progressBar = findViewById(R.id.progress_bar);

        // MainActivity에서 전달된 텍스트 가져오기
        String text = getIntent().getStringExtra("text");
        textView.setText(text);

        String data = textView.getText().toString();

        Thread thread = new Thread(new Runnable() {
            @Override
            public void run() {

                try {
                    OkHttpClient client = new OkHttpClient();
                    MediaType mediaType = MediaType.parse("application/x-www-form-urlencoded");
                    RequestBody body = RequestBody.create(
                            "url=" + URLEncoder.encode(data, "UTF-8"), mediaType);
                    Request request = new Request.Builder()
                            .url("http://127.0.0.1:8000/check/")
                            .post(body)
                            .build();
                    Response response = client.newCall(request).execute();
                    String responseBody = response.body().string();
                    str = responseBody;
                    Log.d("HTTP response", responseBody);
                } catch (IOException e) {
                    Log.d("HTTP", "responseno");
                    e.printStackTrace();
                }
            }
        });
        thread.start();

        // 임시 함수 구현
        new Handler().postDelayed(new Runnable() {
            @Override
            public void run() {
                if (tempFunction()) {
                    // 새로운 액티비티를 시작하고 로딩 화면 종료
                    Intent intent = new Intent(LoadingScreenActivity.this, ResultActivity.class);
                    intent.putExtra("text", str);
                    startActivity(intent);
                    finish();
                } else {
                    // tempFunction이 false를 반환하면 메인 화면으로 돌아감
                    finish();
                }


            }
        }, 5000);
    }


    @Override
    public void onBackPressed() {
        // 아무런 동작도 하지 않음
    }
    private boolean tempFunction() {
        // 임시 함수 구현
        return true;
    }
}