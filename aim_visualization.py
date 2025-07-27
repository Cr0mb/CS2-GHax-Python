import os
import json
import plotly.graph_objs as go
from plotly.offline import plot

LEARN_DIR = "aimbot_data"

files = [f for f in os.listdir(LEARN_DIR) if f.endswith(".json")]
weapon_ids = [f[:-5] for f in files]

if not weapon_ids:
    print("No weapon JSON files found in 'aimbot_data' directory.")
    exit(1)

all_data = {}
for wid in weapon_ids:
    filepath = os.path.join(LEARN_DIR, f"{wid}.json")
    with open(filepath, "r") as f:
        all_data[wid] = json.load(f)

fig = go.Figure()

trace_visibility = []

for weapon_index, weapon_id in enumerate(weapon_ids):
    data = all_data[weapon_id]
    traces_for_weapon = []
    for key, vectors in data.items():
        x, y = [0], [0]
        inv_x, inv_y = [0], [0]
        for dx, dy in vectors:
            x.append(x[-1] + dy)
            y.append(y[-1] + dx)
            inv_x.append(inv_x[-1] - dy)
            inv_y.append(inv_y[-1] - dx)

        recoil_trace = go.Scatter(
            x=x, y=y, mode='lines+markers',
            name=f"Recoil path {key}",
            opacity=0.5,
            marker=dict(size=6),
            line=dict(width=2),
            visible=(weapon_index == 0)
        )
        comp_trace = go.Scatter(
            x=inv_x, y=inv_y, mode='lines+markers',
            name=f"Compensation {key}",
            opacity=0.5,
            line=dict(width=2, dash='dash'),
            marker=dict(size=6),
            visible=(weapon_index == 0)
        )
        traces_for_weapon.extend([recoil_trace, comp_trace])

    center_trace = go.Scatter(
        x=[0], y=[0], mode='markers',
        name="Center (0,0)",
        marker=dict(size=15, color='blue', line=dict(width=2, color='black')),
        visible=(weapon_index == 0)
    )
    traces_for_weapon.append(center_trace)

    fig.add_traces(traces_for_weapon)
    trace_visibility.append(traces_for_weapon)

buttons = []
num_traces_per_weapon = len(trace_visibility[0])

for i, weapon_id in enumerate(weapon_ids):
    visibility = []
    for w in range(len(weapon_ids)):
        visibility.extend([w == i] * num_traces_per_weapon)

    buttons.append(dict(
        label=weapon_id,
        method="update",
        args=[{"visible": visibility},
              {"title": f"Recoil Traces and Compensation - Weapon {weapon_id}"}]
    ))

fig.update_layout(
    updatemenus=[dict(
        buttons=buttons,
        direction="down",
        showactive=True,
        x=0,
        y=1.15,
        xanchor='left',
        yanchor='top',
        pad={"r": 10, "t": 10},
        bgcolor='rgba(0,0,0,0.3)',
        font=dict(color='white')
    )],
    title=f"",
    xaxis_title="Yaw Movement",
    yaxis_title="Pitch Movement",
    yaxis_scaleanchor="x",
    template='plotly_dark',
    legend=dict(bordercolor="LightGray", borderwidth=1),
    hovermode='closest',
    margin=dict(l=10, r=10, t=80, b=40),
    autosize=True,
)

plot(fig, filename='recoil_compensation_viewer.html', auto_open=True, config={'responsive': True})
