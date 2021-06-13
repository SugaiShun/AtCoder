#include <bits/stdc++.h>
using namespace std;

void solve() {

    

    // cout << ans << "\n";
}

signed main() {
    
    int N, Q;
    cin >> N >> Q;

    vector<int> A(N);
    for (int i = 0; i < N; i++) {
        cin >> A.at(i);
    }

    vector<int> rslt(Q);
    for (int i=0; i<Q; i++){
        int k,cnt=0;
        cin >> k;
        for(int j=0; j<N; j++){
            if(A[j]<=(k+cnt)){
                cnt++;
            }
        }
        rslt.at(i)=k+cnt;
    }

    for (int i=0; i<Q; i++){
        cout << rslt.at(i) << endl;
    }

    return 0;
}