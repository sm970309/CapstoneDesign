package com.example.yeartube;

import static java.sql.DriverManager.println;

import android.app.ProgressDialog;
import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

import com.android.volley.AuthFailureError;
import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;

import java.util.HashMap;
import java.util.Map;


public class EnterlinkActivity extends AppCompatActivity {

    static RequestQueue requestQueue;
    Button btn_send_link;
    EditText edit_youtube_link;
    String text;
    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.enterlink_activity);

        edit_youtube_link = (EditText) findViewById(R.id.edit_youtube_link);
        btn_send_link = (Button) findViewById(R.id.btn_send_link);
        text = edit_youtube_link.getText().toString();
        text = "https://www.youtube.com/shorts/F8ECf8Vo_P0";
        String url = "https://267d-117-16-244-19.ngrok-free.app/";
        btn_send_link.setOnClickListener(new View.OnClickListener() {

            @Override
            public void onClick(View view) {
                makeRequest();
            }
        });

        if (requestQueue == null) {
            requestQueue = Volley.newRequestQueue(getApplicationContext());
        }
    }
        public void makeRequest() {
            String url = edit_youtube_link.getText().toString();

            StringRequest request = new StringRequest(Request.Method.POST,
                    "https://267d-117-16-244-19.ngrok-free.app/check/",
                new Response.Listener<String>() {
                        @Override
                        public void onResponse(String response) {
                            Intent intent = new Intent(getApplicationContext(), ResultActivity.class);
                            intent.putExtra("text", response);
                            startActivity(intent);
                        }
                    },
                    new Response.ErrorListener() {
                        @Override
                        public void onErrorResponse(VolleyError error) {
                            //Log.e("error response",error.getMessage());
                            Intent intent = new Intent(getApplicationContext(), LoadingScreenActivity.class);
                            startActivity(intent);
                        }
                    }
            ) {
                @Override
                protected Map<String, String> getParams() throws AuthFailureError {
                    Map<String, String> params = new HashMap<String, String>();
                    params.put("url",text);
                    return params;
                }

            };

            request.setShouldCache(false);
            requestQueue.add(request);
        }

}

